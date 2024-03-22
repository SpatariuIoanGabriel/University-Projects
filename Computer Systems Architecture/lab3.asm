bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; E= [(a-b)*3+c*2]-d
    ; -39
    a db -11
    b db -2
    c db -1
    d dw 10

; our code starts here
segment code use32 class=code
    start:
        ;a-b
        movsx ax, byte[a]
        mov bl, [b]
        movsx bx, bl
        sub ax, bx; ax= a-b
        
        ;(a-b)*3
        mov bx, 3
        imul bx; dx:ax=(a-b)*3
        
        mov cx, dx
        mov bx, ax; cx:bx=(a-b)*3
        
        ;c*2
        movsx ax, byte[c]
        mov dx, 2
        imul dx; dx:ax=c*2
        
        ;(a-b)*3+c*2
        add ax, bx
        adc dx, cx ; dx:ax=(a-b)*3+c*2
        
        push dx
        push ax
        pop eax ; eax= (a-b)*3+c*2
        
        ;[(a-b)*3+c*2]-d
        ;  doubleword - word
        movsx ebx, word[d] ;ebx= d
        sub eax, ebx; eax= [(a-b)*3+c*2]-d
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
