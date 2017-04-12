function submit1()
{
    alert('get');
  var form = new FormData();
  form.append("username",document.getElementById("inputEmail3").value;);
  form.append("password",document.getElementById("inputPassword3").value;);
 jQuery.ajax({

            type:"POST",
            url:"http://1.deveple.applinzi.com/login",
            data:form,
            datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
            beforeSend:function(){var name = document.getElementById("inputEmail3").value;
var password = document.getElementById("inputPassword3").value;
if(!name)
{
    
    alert("please input name");
}
if(!password)
{

alert("please input password");
}},            
            success:function(data){
                       
                alert(data);
            },
            complete: function(XMLHttpRequest, textStatus){
               alert(XMLHttpRequest.responseText);
               alert(textStatus);

            },
            error: function(){
            }         
         });

}