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
    ; A string of words S is given. Compute string D containing only low bytes from string S,
    ; If S = 1234h, 5678h, 1a2bh => D=34h, 78h, 2bh
    
    S dw 1234h, 5678h, 1a2bh
    
    ls equ($-S)/2
    D resb ls
    format db "%x ", 0

; our code starts here
segment code use32 class=code
    start:
        mov ecx, ls
        mov esi, 0
        mov edi, 0
        
        repeta:
            mov al, [S+esi]
            mov [D+edi], al
            add esi, 2
            add edi, 1
        loop repeta
        
        mov ecx, edi
        mov esi, 0
        repeta_afisare
            pushad
            
            movsx eax, byte [D+esi]
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
