###External Module Used###
# Click-shell - An extension to click that easily turns your click app into a shell utility
# requests - Requests is an elegant and simple HTTP library for Python
# termcolor - ANSI color formatting for output in terminal
# coloroma-Simple cross-platform colored terminal text in Python
# python-whois  - Create a simple importable Python module which will produce parsed WHOIS data for a given domain.
# dns.resolver - resolve dns to get ip, and some records A, CNAME, AAAA

###Internal Module Used###
# os - The main purpose of the OS module is to interact with your operating system. The primary use I find for it is to create folders, remove folders, move folders, and sometimes change the working directory.
# datetime-Basic date and time types, the datetime module can support many of the same operations, but provides a more object oriented set of types, and also has some limited support for time zones.
# time - The time module is principally for working with Unix time stamps; expressed as a floating point number taken to be seconds since the Unix epoch.
#socket - Low-level networking interface, A TLS/SSL wrapper, Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection.
#re - Regular expression operations, A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern or regualar expression to concatenet ordinary characters
# json - javascript object notation


from click_shell import shell
import os, requests, time
from datetime import datetime
from termcolor import colored
from colorama import Fore
import whois, socket, re, json
import dns.resolver


#version control & contributer
print(Fore.LIGHTYELLOW_EX + '💳 v0.0.4 🚀')
time.sleep(2)
print(Fore.LIGHTYELLOW_EX + 'BCY Team 19 - VITB ⭐❤️')
time.sleep(3)
print(Fore.LIGHTBLUE_EX + ' ')


@shell(prompt="a_osint > ", intro="""
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗      ██║   ██║███████╗██║██╔██╗ ██║   ██║   
██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝      ██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗    ╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
                                                                                    BCY Team 19 - VITB
Type "Help" for intruction & Usage 
""")


# Shell Prompt by Defined Function that, execute over time to time unitl user passes any command, line 408
def ao_shell():
    pass


# Shell prompt help command
@ao_shell.command()
def help():
    print("""
    Pass alias "cms, sub, dac, ccbin, exit"
    [1] CMS Checker, "cms"
    [2] Subdomain Scanner, "sub"
    [3] Domain Info Check, "dinc"
    [4] Domain Email Grabber, "deg"
    [5] Mass Credit Card Bin Checker, "ccbin"
    [6] User Agent Info, "uai"
    [7] Find IP address and emailserver, "fipes"
    [8] Website Bio Data, "wbo"
    [9] Scan Port for website, "spw"
    [10] Exit, "exit"
    """)


#credit card ke file output ko file bana kar print karna h
def writeFileOutput(data, file, mode="a"):
    f = open(file, mode)
    f.write("{}\n".format(data))
    f.close()
    # After credit card checked it provide output in terminal where as automatically exported to file of an  output result..
    if "|Live|" in data:
        print(colored(data, "green", attrs=["bold"]))
    elif "|Dead|" in data:
        print(colored(data, "red", attrs=["bold"]))
    else:
        print(colored(data, "yellow", attrs=["bold"]))



#Currently this feature is under Contruction Due to API Error/Limitation of Free Plan, website used whatcms.org
@ao_shell.command()
def cms():
    print(Fore.GREEN + """
    ---->Content Management System Checker<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    print(Fore.RED + ' ')
    url = 'https://whatcms.org/others/WhatCMS/API/Tech?key=wnw0d50lcf3dn4a4uuoldtqnroq1o4od4ir8lecqxkowamcar7m76r25z27omiiebtw1q1&url='+ site
    request = requests.get(url)
    responseObject = json.loads(request)
    print('WebSite:', site)
    if responseObject['result']['code'] == 200:
        print('CMS:', responseObject['result']['name'])
        print('Version:', responseObject['result']['version'])
    elif responseObject['result']['code'] == 201:
        print('CMS: Not Found')
    elif responseObject['result']['code'] == 111:
        print('ERROR: Invalid Url')
    elif responseObject['result']['code'] == 101:
        print('Invalid API Key')
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')



#subdomain scanning pagesinventory.com use kiye h
@ao_shell.command()
def sub():
    print(Fore.GREEN + """
    ---->SubDomain Scanner<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    url = 'https://www.pagesinventory.com/search/?s=' + site
    request = requests.get(url)
    response = request.content.decode('utf-8')
    ip = socket.gethostbyname(site)
    print('Website:', site)
    print('IP:', ip, '\n')
    if 'Search result for' in response:
        match = r'/domain/(.*?).html(.*?)/ip/(.*?).html'
        if re.search(match, response):
            a = 0
            for i in re.findall(match, response):
                a = a + 1
                print(a)
                print('Website:', i[0])
                print('IP:', i[2], '\n')
                time.sleep(1)
            print('All Subdomain Listed/If not means website has no subdomain')
    elif 'Nothing was found' in response:
        print('No Subdomains Found For This Domain')



#python-whois se enumeration
@ao_shell.command()
def dinc():
    print(Fore.GREEN + """
    ---->Domain Info CHECKER<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    #whois module se whois org website se site ki full information ⬇️
    w = whois.whois(site)
    print(Fore.LIGHTYELLOW_EX + ' ')
    print(w)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')



#python-whois se enumeration email ki domain ka
@ao_shell.command()
def deg():
    print(Fore.GREEN + """
    ---->Domain Email Grabber<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    #whois module se whois org website se site,email ki full information ⬇️
    emails = whois.whois(site).emails
    print(Fore.LIGHTYELLOW_EX+ ' ')
    print(emails)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')



@ao_shell.command()
def uai():
    print(Fore.GREEN + """
    ---->User Agent Info<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    useragent = useragent.replace('/', '%2F')
    useragent = useragent.replace(' ', '%20')
    useragent = useragent.replace('(', '%28')
    useragent = useragent.replace(';', '%3B')
    useragent = useragent.replace(':', '%3A')
    useragent = useragent.replace(')', '%29')
    useragent = useragent.replace(',', '%2C')

    url = 'http://api.userstack.com/api/detect?access_key=dbee475db3243e4eaa9d932eb7194f35' + '&ua=' + useragent + '& output = json'
    request = requests.get(url)
    print(Fore.LIGHTYELLOW_EX+ ' ')
    print(request.json())
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')



@ao_shell.command()
def fipes():
    print(Fore.GREEN + """
    ---->Find IP address and emailserver<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    print(Fore.LIGHTYELLOW_EX+ ' ')
    result = dns.resolver.resolve(site, 'A')
    for ipval in result:
        print('IP', ipval.to_text())
    print("This domain has no email")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    


# Credit card bin checker functionality
# used - https://www.xchecker.cc/api-man.php - bulk credit card check 
@ao_shell.command()
def ccbin():
    print("""
    ---->Mass Credit Card Bin CHECKER<----
    """)
    print(Fore.LIGHTYELLOW_EX + """Create a file name \"cc.txt\" in same directory paste your credit card 
    Example. 
    Use format ccNumber|expMonth|expYear|cvc -> 4140918523888721|01|2025|791
    """)
    #ham yaha par user cc.txt file banne ka time de rahe h
    input("Press Enter to continue...If Created")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    ccFile = "cc.txt"
    outputFile = "cc_checked_{}.txt".format(int(datetime.timestamp(datetime.now())))
    checkerAPIURL = "https://www.xchecker.cc/api.php?cc={}|{}|{}|{}"
    headers = { 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
        "Accept": "*/*",
        }
    if os.path.exists(ccFile):
        with open(ccFile) as f:
            writeFileOutput("Output file results: {}".format(outputFile), outputFile)
            for cc in f:
                cc = cc.replace("\r", "").replace("\n", "")
                try:
                    ccNumber = cc.split("|")[0]
                    expMonth = cc.split("|")[1]
                    expYear = cc.split("|")[2]
                    cvc = cc.split("|")[3]
                except:
                    writeFileOutput("{} => Format error. Use ccNumber|expMonth|expYear|cvc".format(cc), outputFile)
                    continue
                url = checkerAPIURL.format(ccNumber, expMonth, expYear, cvc)
                while True:
                    response = requests.get(url, headers=headers, verify=False, allow_redirects=False)
                    if response.status_code == 200 and "json" in response.headers["Content-Type"]:
                        data = response.json()
                        if "ccNumber" in data:
                            output = data["ccNumber"]
                            if "cvc" in data:
                                output = data["cvc"]
                            if "expMonth" in data:
                                output += "|>|" + data["expMonth"]
                                output += "/" + data ["expYear"]
                            output += " |>| " + data["status"] + " |>| " + data["details"]
                            output += " |>| " + data["bankName"]
                        else:
                            output = "{} => {}".format(ccNumber, data["error"])
                        writeFileOutput(output, outputFile)
                        break
                    else:
                        writeFileOutput("HTTP service error: {}, retry...".format(response.status_code), outputFile)
    else:
        print("File {} not found in current directory".format(ccFile))            



@ao_shell.command()
def wbo():
    print(Fore.GREEN + """
    ---->Website Bio Data<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    url = 'https://myip.ms/' + site
    request = requests.get(url)
    print(Fore.LIGHTYELLOW_EX+ ' ')
    response = request.content.decode('utf-8')
    if re.search(r'([,\d]+) visitors per day', response):
        print( 'Hosting Info for Website:', site)
        print( 'Visitors per day:', re.search(r'([,\d]+) visitors per day', response)[1])
        print( 'IP Address:', socket.gethostbyname(site))
        match = re.search(r"/whois6/((.*?))'", response)
        if match:
            print( 'Linked IPv6 Address:', match[1])
        match = re.search(r"IP Location: <(.*?)html'>(.*?)<", response)
        if match:
            print( 'IP Location:', match[2])
        match = re.search(r"<b>IP Reverse DNS(.*?)'>(.*?)<", response)
        if match:
            print( 'IP Reverse DNS (Host):', match[2])
        match = re.search(r"'nounderline'><a title='((.*?))'", response)
        if match:
            print( 'Hosting Company:', match[1])
        match = re.search(r"Hosting Company \/ IP Owner: <(.*?)html'>(.*?)<", response)
        if match:
            print( 'Hosting Company IP Owner:', match[2])
        match = re.search(r'IP Range <b>(.*?) - (.*?)<(.*?)<b>(.*?)<', response)
        if match:
            print( 'Hosting IP Range:', match[1], '-', match[2], '('+ match[4], 'ip)')
        match = re.search(r"Hosting Address: <\/td><td>((.*?))<", response)
        if match:
            print( 'Hosting Address:', match[1])
        match = re.search(r"Owner Address: <\/td><td>((.*?))<", response)
        if match:
            print( 'Owner Address:', match[1])
        match = re.search(r"Hosting Country: <(.*?)html'>(.*?)<", response)
        if match:
            print( 'Hosting Country:', match[2])
        match = re.search(r"Owner Country: <(.*?)html'>(.*?)<", response)
        if match:
            print( 'Owner Country:', match[2])
        match = re.search(r'Hosting Phone: <\/td><td>((.*?))<', response)
        if match:
            print( 'Hosting Phone:', match[1])
        match = re.search(r"Owner Phone: </td><td>((.*?))<", response)
        if match:
            print( 'Owner Phone', match[1])
        match = re.search(r"> Hosting Website: <(.*?)a href='/(.*?)'", response)
        if match:
            print( 'Hosting Website:', match[2])
        match = re.search(r"Owner Website: <(.*?)href='/(.*?)'", response)
        if match:
            print( 'Owner Website:', match[2])
        match = re.search(r'CIDR:<\/td><td> (.*?)<', response)
        if match:
            print('CIDR:', match[1])
        match = re.search(r'Owner CIDR: <(.*?)ip_addresses/(.*?)">(.*?)</a>(.*?)<', response)
        if match:
            print('Owner CIDR:', match[3] + match[4])
        match = re.search(r'Hosting CIDR: <(.*?)ip_addresses/(.*?)">(.*?)</a>(.*?)<', response)
        if match:
            print('Hosting CIDR:', match[3] + match[4])
        url = 'https://dns-api.org/NS/' + site
    else:
        print("Info not avaliable right now !!")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')



@ao_shell.command()
def spw():
    print(Fore.GREEN + """
    ---->Scan Port for website<----
    """)
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')
    site = input(' Enter Website : ')
    ip = socket.gethostbyname(site)
    print('PORT     STATE       SERVICE')
    ports = {21: 'FTP',
             22: 'SSH',
             23: 'Telnet',
             25: 'SMTP',
             43: 'Whois',
             53: 'DNS',
             68: 'DHCP',
             80: 'HTTP',
             110: 'POP3',
             115: 'SFTP',
             119: 'NNTP',
             123: 'NTP',
             143: 'IMAP',
             161: 'SNMP',
             220: 'IMAP3',
             389: 'LDAP',
             443: 'SSL',
             1521: 'Oracle SQL',
             2049: 'NFS',
             3306: 'mySQL',
             5800: 'VNC',
             8080: 'HTTP'}
    print(Fore.LIGHTYELLOW_EX+ ' ')
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(str(port) + '         '[len(str(port)):] + 'Open' + '        ' + ports[port])
        else:
            print(str(port) + '         '[len(str(port)):] + 'Closed' + '      ' + ports[port])
        sock.close()
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + ' ')



if __name__ == '__main__':
    ao_shell()
