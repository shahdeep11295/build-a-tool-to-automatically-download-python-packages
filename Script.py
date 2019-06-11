# pip:version 9.3.0


import sys, os,json
import pip
class Script:

	def __init__(self):
		self.cmd="sudo pip install "
		self.dicElem={}
		self.existdicts={}
		self.dict3={}


	def getData(self,name):
		f=open(name,'r')
		data=json.load(f);
		self.dicElem=data.get("Dependencies")
		f.close()

	def getExistedDependencies(self):
		
		d_packages = pip.get_installed_distributions(local_only=True)
		d_packages_list = sorted(["%s==%s" % (i.key, i.version)
			for i in d_packages])

		for ele in d_packages_list:
			var=ele.split("==")
			self.existdicts[var[0]]=var[1]

	def getJsonDependenciesInstalled(self):
		for key,val in self.dicElem.items():
			os.system(self.cmd+str(key)+"=="+str(val))

	def checkAnyUninstalled(self,):
		for i,j in self.dicElem.items():
			if i in self.existdicts:
				if j==self.existdicts[i]:
					print(i+" is successfully installed\n")
				else:
					self.dict3[i]=j;
			else:
				self.dict3[i]=j;

		print("####\n")
		print("*Install Failed Dependencies*\n")
		for k,v in self.dict3.items():
			print(k+" of version "+v+" not installed")
		print("#####")


if __name__ == '__main__':
	obj=Script()

	obj.getData("Dependencies.json")
	
	obj.getJsonDependenciesInstalled()

	obj.getExistedDependencies()

	obj.checkAnyUninstalled()
