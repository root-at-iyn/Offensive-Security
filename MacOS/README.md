# MacOS Security

### This section aims to cover content related to MacOS Security and Internals. I've found it hard to find good Offensive Security content for the MacOS enviroment (at least compared to Windows) so I'm attempting to make things better

# Quick Resources

## Repositories

- [Awesome-macOS-Red-Teaming](https://github.com/tonghuaroot/Awesome-macOS-Red-Teaming)
- [osx-abi-macho-file-format-reference](osx-abi-macho-file-format-reference)
- [SwiftBelt](https://github.com/cedowens/SwiftBelt)
- [EntitlementCheck](https://github.com/cedowens/EntitlementCheck)
- [Persistent-Swift](https://github.com/cedowens/Persistent-Swift)
- [SwiftSpy](https://github.com/slyd0g/SwiftSpy)
- [DylibHijackTest](https://github.com/slyd0g/DylibHijackTest)
- [ObjCShellcodeLoader](https://github.com/slyd0g/ObjCShellcodeLoader)
- [TCC-ClickJacking](https://github.com/breakpointHQ/TCC-ClickJacking)
- [Apple Open Source Releases - (MacOS, iOS, DevTools)](https://opensource.apple.com/releases/)
- [XNU Kernel](https://github.com/apple-oss-distributions/xnu)
- [WebKit](https://github.com/apple-oss-distributions/WebKit)
- [iOS-messaging-tools](https://github.com/googleprojectzero/iOS-messaging-tools)


## Apple Developer Docs

- [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210)
- [Foundation Framework for MacOS, iOS ... *OS](https://developer.apple.com/documentation/foundation?language=objc)
- [Security Framework](https://developer.apple.com/documentation/security?language=objc)
- [Apple CryptoKit](https://developer.apple.com/documentation/cryptokit?language=objc)
- [Apple Silicon](https://developer.apple.com/documentation/apple-silicon?language=objc)
- [Kernel Framework](https://developer.apple.com/documentation/kernel)


## Red Team Writeups

- [How AppleScript Is Used For Attacking macOS](https://www.sentinelone.com/blog/how-offensive-actors-use-applescript-for-attacking-macos/)
- [macOS Red Team: Calling Apple APIs Without Building Binaries](https://www.sentinelone.com/blog/macos-red-team-calling-apple-apis-without-building-binaries/)
- [macOS Red Team: Spoofing Privileged Helpers (and Others) to Gain Root](https://www.sentinelone.com/blog/macos-red-team-spoofing-privileged-helpers-and-others-to-gain-root/)
- [GateKeeper - Not a Bypass (Again)](https://theevilbit.github.io/posts/gatekeeper_not_a_bypass/)
- [Persistent Credential Theft with Authorization Plugins](https://posts.specterops.io/persistent-credential-theft-with-authorization-plugins-d17b34719d65)
- [Beyond the good ol' LaunchAgents - 28 - Authorization Plugins](https://theevilbit.github.io/beyond/beyond_0028/)
- [Working Around macOS Privacy Controls in Red Team Ops](https://cedowens.medium.com/initial-access-checks-on-macos-531dd2d0cee6)
- [Taking ESF For A(nother) Spin](https://medium.com/@cedowens/taking-esf-for-a-nother-spin-6e1e6acd1b74)
- [Abusing Slack for Offensive Operations](https://posts.specterops.io/abusing-slack-for-offensive-operations-2343237b9282)
- [In-Memory Execution in macOS: the Old and the New](https://rtx.meta.security/post-exploitation/2022/12/19/In-Memory-Execution-in-macOS.html)


## Malware Analysis

- [The Art of Mac Malware](https://nostarch.com/art-mac-malware) - (Book by Patrick Wardle)


## Zero-Day / N-Day Writeups

- [CVE-2021-30808 - CVE-2021-1784 strikes back - TCC bypass via mounting](https://theevilbit.github.io/posts/cve-2021-30808/)
- [Get root on macOS 13.0.1 with CVE-2022-46689, the macOS Dirty Cow bug](https://worthdoingbadly.com/macdirtycow/)
- [A deep dive into an NSO zero-click iMessage exploit: Remote Code Execution](https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html?m=1)
- [A very deep dive into iOS Exploit chains found in the wild](https://googleprojectzero.blogspot.com/2019/08/a-very-deep-dive-into-ios-exploit.html)
- [CVE-2021-1782, an iOS in-the-wild vulnerability in vouchers](https://googleprojectzero.blogspot.com/2022/04/cve-2021-1782-ios-in-wild-vulnerability.html)
- [CVE-2022-22620: Use-after-free in Safari](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2022/CVE-2022-22620.html)
- [An Autopsy on a Zombie In-the-Wild 0-day](https://googleprojectzero.blogspot.com/2022/06/an-autopsy-on-zombie-in-wild-0-day.html)
- [Writing an iOS Kernel Exploit from Scratch](https://secfault-security.com/blog/chain3.html)
- [CVE-2021-1879: Use-After-Free in QuickTimePluginReplacement](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1879.html)


## Conference Talks (Video)

- [Objective by the Sea, v5.0](https://www.youtube.com/playlist?list=PLliknDIoYszt5m1kz1vNY90LnR6VMuyOZ)
- [Objective by the Sea, v4.0](https://www.youtube.com/playlist?list=PLliknDIoYszvjA1Lix-Uce7ZDxS39J2ZY)
- [Behind the scenes of iOS and Mac Security](https://youtu.be/3byNNUReyvE)
- [Mythic Feature Examples](https://youtube.com/playlist?list=PLHVFedjbv6sNLB1QqnGJxRBMukPRGYa-H)
- [Heap Overflow on iOS/Android ARM64](https://youtu.be/CmTA05bcawk)
- [Look, No Hands! -- The Remote, Interaction-less Attack Surface of the iPhone](https://youtu.be/ySxzkBSFkxQ)
- [DEF CON 29 - Patrick Wardle - Bundles of Joy: Breaking MacOS via Subverted Applications Bundles](https://youtu.be/raSTgFqYaoc)
