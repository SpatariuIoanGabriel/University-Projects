bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; E1= (d-b*c+b*2)/a
    a db 5
    b db 2
    c db 3
    d dw 12

; our code starts here
segment code use32 class=code
    start:
        ;b*c
        mov al,[b]
        mov bl,[c]
        mul bl; ax=b*c
        
        ;d-b*c
        ;word - word
        mov bx, [d]
        sub bx, ax; bx = d-b*c
       
        ;b*2
        mov al,[b]
        mov cl, 2
        mul cl; ax=b*2
       
        ;d-b*c+b*2
        add ax, bx; ax= d-b*c+b*2
        
        ;(d-b*c+b*2)/a
        ; word       byte
        div byte[a]; (d-b*c+b*2)/a -> al=cat
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
