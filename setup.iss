[Setup]
AppName=Gerador de Peças DXF
AppVersion=1.0
DefaultDirName={pf}\Gerador de Peças DXF
DefaultGroupName=Gerador de Peças DXF
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\maquina.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Gerador de Peças DXF"; Filename: "{app}\maquina.exe"; IconFilename: "{app}\icon.ico"
Name: "{commondesktop}\Gerador de Peças DXF"; Filename: "{app}\maquina.exe"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\maquina.exe"; Description: "{cm:LaunchProgram,Gerador de Peças DXF}"; Flags: nowait postinstall skipifsilent