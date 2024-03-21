bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern printf                          
import printf msvcrt.dll                          

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A string of bytes A is given. Construct string B containing only values divisible with 7 from string A. 
    ;If A= 12,13,14,18,21 => B= 14,21

    A db 12, 13, 14, 18, 21
    
    ls equ($-A)
    B resb ls
    format db "%d ", 0
    
; our code starts here
segment code use32 class=code
    start:
        mov ecx, ls
        mov esi, 0
        mov edi, 0
        mov bl, 7
        repeta:
            movsx ax, byte[A+esi]
   
            idiv bl; al= cat, ah= rest
            
            cmp ah, 0
            Je introduce
            Jmp next
            
            introduce:
                mov dl,[A+esi]
                mov [B+edi], dl
                add edi, 1
                
            next:
            
        add esi, 1 
        
        loop repeta
        
        mov ecx, edi
        mov esi, 0
        repeta_afisare
            pushad
            
            movsx eax, byte [B+esi]
            push eax
            push dword format
            call [printf]
            add esp, 4*2
            popad

            add esi, 1
      
        loop repeta_afisare
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
