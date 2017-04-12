
/**
 * Created by xq on 2017/4/1.
 */
function randomNum(min,max)
{
return Math.floor(Math.random()*(max-min)+min);
}
function randomColor(min,max)
{
 r = randomNum(min,max);
 g = randomNum(min,max);
 b = randomNum(min,max);
 return "rgb("+r+","+g+","+b+")";
}

function drawPic()
{
var can = document.getElementById("canvas");
var height = can.height;
var weight = can.width;
var ctx = can.getContext("2d");
ctx.textBaseline = "bottom";
ctx.fillStyle = randomColor(180,240);
ctx.fillRect(width,height);
var strNum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
for(var i = 0;i<4;i++)
{
    var txt = strNum[randomNum(0,strNum.length)];
    ctx.fillStyle = randomColor(50,160);
    ctx.font = randomNum(15,40)+"px SimHei";
    var x = i*10+25;
    var y = randomNum(25,40);
    var deg = randomNum(-45,45);
    ctx.translate(x,y);
    ctx.rotate(deg*Math.PI/180);
    ctx.fillText(txt,0,0);
    ctx.rotate(-deg*Math.PI/180);
    ctx.translate(-x,-y);
}

}
