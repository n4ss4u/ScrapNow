import whois
import dns.resolver
import sys
import os
import requests
import platform
from colorama import Fore as f, Back as b
from bs4 import BeautifulSoup


target = sys.argv[1]
target = target.replace("https://", "")
target = target.replace("http://", "")


if platform.system() == "Windows":
	os.system("cls")

elif platform.system() == "Linux":
	os.system("clear")


response = requests.get("https://" + target)

print("COMUNIDAD DE TELEGRAM: https://t.me/agoralatam\n")
#OBTENER INFORMACION BÁSICA 
print(f.RESET + "══════════ INFORMACION BASICA ═════════")
domain_info = whois.whois(target)
try:
	print(f.CYAN + "ORGANIZACION: " + f.BLUE + domain_info.org + f.CYAN + "\nUBICACION: " + f.BLUE + domain_info.state, domain_info.country + f.CYAN + "\nDOMINIO: " + f.BLUE + domain_info.domain_name[1] + f.CYAN + "\nFECHA DE CREACION: " + f.BLUE + domain_info.creation_date[0] + f.CYAN + "\nFECHA DE EXPIRACION: " + f.BLUE + domain_info.expiration_date[0] + "\n")
except TypeError:
	print(f.CYAN + "ORGANIZACION: " + f.BLUE + domain_info.org + f.CYAN + "\nUBICACION: " + f.BLUE + domain_info.state, domain_info.country + f.CYAN + "\nDOMINIO: " + f.BLUE + domain_info.domain_name[1] + f.CYAN + "\nFECHA DE CREACION: " + f.BLUE + "Indeterminada" + f.CYAN + "\nFECHA DE EXPIRACION: " + f.BLUE + "Indeterminada\n" + f.RESET)


list_results = []
ipv4 = ""
ipv6 = ""
dns_servers = ""
email_servers = ""
domain_verification = ""


#OBTENER IPV4
try: 
	request = dns.resolver.resolve(target, "A")
	for i in request:
		ipv4 += str(i) + "\n"
except:
	ipv4 = f.CYAN + "Indeterminada\n"

list_results.append(ipv4)

print(f.RESET + "\n═════════════════ IPV4 ════════════════\n" + f.CYAN + list_results[0])




#OBTENER IPV6
try:
	request = dns.resolver.resolve(target, "AAAA")
	for i in request:
		ipv6 += str(i) + "\n"

except:
	ipv6 = f.CYAN + "Indeterminada\n"

list_results.append(ipv6)

print(f.RESET + "\n═════════════════ IPV6 ════════════════\n" + f.CYAN + list_results[1])




#OBTENER SERVIDORES DNS
try:
	request = dns.resolver.resolve(target, "NS")

	for i in request:
		dns_servers += str(i) + "\n"

except:
	dns_servers = f.CYAN + "Indeterminada\n"

list_results.append(dns_servers)

print(f.RESET + "\n══════════ SERVIDORES DE DNS ══════════\n" + f.CYAN + list_results[2])




#ONTENER SERVIDORES DE CORREO 
try:
	request = dns.resolver.resolve(target, "MX")
	for i in request:
		email_servers += str(i) + "\n"
except:
	email_servers = f.CYAN + "Indeterminada\n"

list_results.append(email_servers)

print(f.RESET + "\n════════ SERVIDORES DE CORREO ═════════\n" + f.CYAN + list_results[3])




#OBTENER VERIFICACIÖN DE DOMINIOS
try:
	request = dns.resolver.resolve(target, "TXT", lifetime=30.0)
	for i in request:
		domain_verification += str(i) + "\n"
except:
	domain_verification = f.CYAN + "Indeterminada\n"

list_results.append(domain_verification)

print(f.RESET + "\n══════ VERIFICAIONES DE DOMINIOS ══════\n" + f.CYAN + list_results[4])




#OBTENER CABECERAS DE RESPUESTAS
headers_target = response.headers

print(f.RESET + "\n═══════ CABECERAS DE RESPUESTA ═══════")

for key, value in headers_target.items():
	print(f.CYAN + value + ":" + f.BLUE + "[" + key + "]" + f.RESET + "\n────────────────────────────────────")




#OBTENER ENLACES INDEXADOS EN EL SITIO
soup = BeautifulSoup(response.text, "html.parser")
a_label = soup.find_all("a")

print(f.RESET + "\n\n══════════ ENLACES INDEXADOS ══════════")

for i in a_label:
	print(f.CYAN + i.get("href") + f.RESET + "\n────────────────────────────────────")


