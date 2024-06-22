<h1 style='color:red'> SSH </h1>
<h3 style='color:blue'>  generating public and private key </h3> &nbsp;

<span style="color:yellow"> ssh-keygen -o -t rsa -C "@hussain" </span> <br>


 then simply press enter enter and enter for the question asked and it will create your public and private key
 then, <br>
<span style="color:yellow"> cd </span> <br>
 (come to your  root directory by doing cd enter) <br><br>
 <span style="color:yellow"> ls -a  </span> 
  {find your .ssh file}
 
<span style="color:yellow"> cd .ssh #here you can find your public key named as id_rsa.pub and private key as id_rsa </span> <br>

open your public key {i.e, id_rsa.pub} and copy it.
open your github account > navigate to top right to your circular profile icon and click and go to the settings > SSH and CPG Keys > New SSH Key
paste your public key here and give a name to the key like 'local key' and then save it ,and your ssh setup is done.


## to know your git remote origin adress {repo name}

<span style="color:yellow"> git remote -v </span>

<span style="color:red">This text is red.</span> <br>
<span style="color:green">This text is green.</span> <br>
<span style="color:blue">This text is blue.</span>

















