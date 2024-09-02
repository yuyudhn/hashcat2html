# hashcat2html

This tool is designed to convert cracked passwords from Hashcat into a formatted HTML table. The motivation behind this tool arises from internal penetration testing engagements, particularly when I've managed to take over a Domain Admin account. In these scenarios, I typically perform credential dumping from the Domain Controller (using techniques like DCSync). Clients often request a list of all users with weak passwords, especially if any user's NTLM password can be cracked using public wordlists like rockyou.txt.

Initially, I developed a Python tool to parse Hashcat pot files and convert them into a PDF report. However, implementing tables in PDFs using Python proved to be quite complex, especially when dealing with issues like wrapping text inside columns. To simplify the process, I decided to generate the report in HTML format instead. This allows the report to be easily viewed in a browser, and the print feature can be used to convert the HTML into a PDF file if needed.

## Usage Instructions
This tool only accept a input file containing this format:
```
evangelion.local\asuka:6127f489b8118f9d8c475f8aa0039fb5:@administrator_hi5
Guest:31d6cfe0d16ae931b73c59d7e0c089c0:
DefaultAccount:31d6cfe0d16ae931b73c59d7e0c089c0:
evangelion.local\rei:b963c57010f218edc2cc3c229b5e4d0f:iloveyou
evangelion.local\shinji:790361d02d372331cba566eb286a8e5a:11admin07
evangelion.local\kaworu:4c090b2a4a9a78b43510ceec3a60f90b:babygirl
evangelion.local\misato:1338c0e714dfe8e77c8391547e3e31b9:bubba1
evangelion.local\toji:ecd647752a1f351e80291e29fa52246b:yahoo2
evangelion.local\gendo:c0d19b7a638ef50c758892d4de880efb:iluvmark2
evangelion.local\ibuki:291df116791db728f5872ccc9291d3f8:september7
```

Cracking NTLM Hashes with Hashcat:
First, crack the NTLM hashes using Hashcat:
```
hashcat -m 1000 samples/secretsdump-ntlm.txt /usr/share/wordlists/rockyou.txt --username --potfile-path=samples/ntlm_cracked_samples.pot
```

Save the cracked results to a different file:
```
hashcat -m 1000 samples/secretsdump-ntlm.txt --username --potfile-path=samples/ntlm_cracked_samples.pot --show | tee samples/cracked_samples.txt
```

Now, use this tool to generate an HTML report:
```
python3 hashcat2html.py -i samples/cracked_samples.txt -t "EVANGELION.LOCAL Cracked Passwords" --output samples/output_sample.html
```

You can view the result in a browser, or use the browser's print feature to save the report as a PDF if needed.

![HTML Output](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhO4Y-ZpHwu5zM8lyuBMcxCNTg_qfFjBgWfz9ZN0uBHLaUARMCqccb9gjF3J1dMGG4LRnFNJ6xxqXA1mRuE08HjPFUL6Ie4wKC6Cav8IzSEhFQY08E4389EZYSLSK4IyIGyHIIzhhnQOwSEiL7wECdXYdkrZp_9rcOaXDF52o4_H8d9R9h-t0GT3wV-7i4/s1915/html%20output.png)

![Print from Browser](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjBv-AM5ENPRri32ICF_mVkVYktXmC0HZzK8v_BKBjZmD6Q5aBARd2giy2qblsy6S2C6mekq_ObVu4LnaIqGx4Nltf1rXugT1bg2iGzGj2hJf63-6lhDVzPPQ-TMwGWjTcbMYjQRVQ2kOBXzdUARbxshqUG4b_J8Ebqfxy0Ta8CSSWWvltvwWYpnCxPYc/s1599/print%20from%20browser.png)

Just like that. Actually, I made this tool as a complement to the amazing tool [graphcat](https://github.com/Orange-Cyberdefense/graphcat), which offers more features for analyzing and generating reports from Hashcat potfiles.

## Contribute
For now, this feature is all I need, but if you'd like to add other features or improve my messy code, feel free to submit a pull request.