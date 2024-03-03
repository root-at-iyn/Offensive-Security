// vAllocExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <Windows.h>
#include <stdio.h>
#include <malloc.h>


int main()
{
    LPVOID lpvBase = nullptr;
    SYSTEM_INFO sSysInfo;
    DWORD dwPageSize;

    GetSystemInfo(&sSysInfo); // initialise GetSystemInfo struct
    dwPageSize = sSysInfo.dwPageSize; // Save page size

    // Allocate one page size of memory 
    lpvBase = VirtualAlloc(
        NULL,
        dwPageSize,
        MEM_RESERVE | MEM_COMMIT,
        PAGE_READWRITE
        );

    // Calculate address range
    LPTSTR lpvLast = (LPTSTR)((ULONGLONG)lpvBase + (dwPageSize - 2)); // Last usuable address
    printf("Base Address: %p\tDecimal: %lu\n", lpvBase, lpvBase);
    printf("Last Address: %p\tDecimal: %lu\n\n", lpvLast, lpvLast);

    // Get memory information
    _MEMORY_BASIC_INFORMATION memInfo;
    VirtualQuery(lpvBase, &memInfo, sizeof(memInfo));

    // WinAPI struct definition
    /*
    typedef struct _MEMORY_BASIC_INFORMATION {
      PVOID  BaseAddress;
      PVOID  AllocationBase;
      DWORD  AllocationProtect;
      WORD   PartitionId;
      SIZE_T RegionSize;
      DWORD  State;
      DWORD  Protect;
      DWORD  Type;
    } MEMORY_BASIC_INFORMATION, *PMEMORY_BASIC_INFORMATION;
    */

    // Print memory info
    printf("The size of allocated memory page is: %zu\n", memInfo.RegionSize);
    printf("Base Address: %p\n", memInfo.BaseAddress);
    printf("Allocation Base: %p\n", memInfo.AllocationBase);
    printf("Allocation Protect: %lu\n", memInfo.AllocationProtect);
    printf("Partition Id: %d\n", memInfo.PartitionId);
    printf("State: 0x%x\n", memInfo.State);
    printf("Protect: 0x%x\n", memInfo.Protect);
    printf("Type: 0x%x\n\n", memInfo.Type);

    ULONGLONG nextAddr;
    for (int i = 0; i < (dwPageSize -1); i++) {
        nextAddr = (ULONGLONG)lpvBase + i;
        *(LPTSTR)nextAddr = 'A';
        printf("[%d] Memory at %p: 0x%X\n", i,(LPTSTR)nextAddr, *(LPTSTR)nextAddr);
    }
    
    // Free Memory
    BOOL memFree;
    memFree = VirtualFree(
        lpvBase,
        0,
        MEM_RELEASE
        );
    getchar();
}


