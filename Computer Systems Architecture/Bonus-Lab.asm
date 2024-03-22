bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first inAuction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fclose, printf, fprintf, fscanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    
import fread msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fscanf msvcrt.dll

			  ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
;A file name try.txt is given in data segment.
;The file try exists and contains 10 numbers in hexadecimal.
;Extract the maximum number and print this maximum into another file try2. The file try2 doesn’t exist (it is necessary to be created first).

	file_name1 db "try.txt", 0 
	file_name2 db "try2.txt" ,0
	access_mode1 db "r", 0
	access_mode2 db "w", 0 
	file_descriptor1 dd -1
	file_descriptor2 dd -1
	input resd 10
	maximum dd 0; 
    format db "%x", 0
; our code starts here
segment code use32 class=code
    start:
        push dword access_mode1
        push dword file_name1

        call [fopen] 

        mov [file_descriptor1], eax

        cmp dword[file_descriptor1] , 0
        je final 

        add esp, 4*2 
      
        
        mov esi, 0
        repeta2:
        lea eax,[input+esi]
        
        pushad
        push dword eax
        push dword format
        push dword[file_descriptor1]
        call [fscanf]
        add esp,4*3
        
        
        cmp eax,1
        jne peste
        popad
        mov edx, [input]
        mov [maximum], edx
        add esi,4
        jmp repeta2
        
        peste:
        mov ecx , 10
        mov esi , 0
        repeta:
            mov eax , dword[input+esi]
            cmp eax,  [maximum]
            jg continua
            jmp next
            continua:
                mov [maximum] ,eax
            next:
            add esi, 4
        loop repeta
        

        push dword access_mode2
        push dword file_name2
        call [fopen] 
        add esp, 4*2 

        mov [file_descriptor2] , eax

        push dword[maximum]
        push dword format
        push dword [file_descriptor2]

        call [fprintf]

        add esp, 4*3 


        push dword [file_descriptor1]
        call [fclose]

        add esp , 4 

        final:


        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
