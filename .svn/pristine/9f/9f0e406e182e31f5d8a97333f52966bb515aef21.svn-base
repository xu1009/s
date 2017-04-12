function identy()
{

var name = document.getElementById("inputEmail3").value;
var password = document.getElementById("inputPassword3").value;

if(!name)
{
    alert("用户名不能为空");
   
}
if(!password)
{
    alert("密码不能为空");

}
    
if(name&&password) //submit
{
 alert("erwe");
$.post("http://1.deveple.applinzi.com/login",{username:name,password:password},function(data){alert(data);})
}
}