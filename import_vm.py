import subprocess

try:

    import_command = r'Import-VM -Path "C:\VM_exports\Virtual Machine_2\Virtual Machines\C404CAC8-C4BD-4B1C-8B7F-2709056BE0AF.vmcx" -VhdDestinationPath "C:\ProgramData\Microsoft\Windows\Virtual Hard Disks\imported_vhd" -VirtualMachinePath "C:\ProgramData\Microsoft\Windows\Virtual Hard Disks\imported_vhd" -Copy -GenerateNewId'
    subprocess.run(["powershell", import_command])

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
