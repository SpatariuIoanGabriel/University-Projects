bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; E2= (2-a*b)/(a*3)-a+c
    a db 1
    b dw 1
    c dd 10
    aux dw 0

; our code starts here
segment code use32 class=code
    start:
        ;a*b
        movzx ax, byte[a]
        mul word[b]; dx:ax=a*b
        
        ;2-a*b
        mov bl, 2
        movzx bx, bl
        mov cx, 0; cx:bx=2
        ;cx:bx-
        ;dx:ax
        sub bx, ax
        sbb cx, dx; cx:bx= 2-a*b
    
        ;a*3
        mov al, [a]
        mov dl, 3
        mul dl; ax= a*3
        mov [aux], ax
       
        ;(2-a*b)     /  (a*3)
        ; doubleword    word
        mov ax, bx
        mov dx, cx
        div word[aux]; (2-a*b)/(a*3), ax=cat
        
        ; (2-a*b)/(a*3)- a
        ;  word           byte
        movzx bx, byte[a]; bx = a
        sub ax, bx; ax = (2-a*b)/(a*3)-a
        
        ;(2-a*b)/(a*3)-a  + c
        ;  word              doubleword
        movzx eax, word ax
        mov ecx, [c]
        add eax, ecx; ebx= (2-a*b)/(a*3)-a+c
       
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
