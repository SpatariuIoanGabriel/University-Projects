bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; if f%3= 0 then e= a*(4+b)
                    ;else e=23 -(-a)
    a db -1
    b dw -2 
    e dd 0
    f db 4

; our code starts here
segment code use32 class=code
    start:
        ; f%3
        movsx ax, byte[f]
        mov bl, 3
        idiv bl; al= cat, ah= rest
        
        cmp ah, 0
        JE ramurathen
        JNE ramuraelse
        
        ramurathen:
        ;e= a*(4+b)
        ;4+b
        mov bx, 4
        add bx, [b]; bx= 4+b
        
        ;a*(4+b)
        movsx ax, byte[a]
        imul bx; dx:ax= a*(4+b)
        
        ;dx:ax->e
        mov word[e+0], ax
        mov word[e+2], dx
        
        jmp myendif
        
        ramuraelse:
        ;e=23 -(-a)
        ;-a
        mov bx, 0
        mov cx, [a]
        sub bx, cx; bx= -a
        
        mov ax, 23
        sub ax, bx; ax=23 -(-a)
        cwd; dx:ax=23 -(-a)
        mov word[e+0], ax
        mov word[e+2], dx
        myendif:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
