var c=document.getElementById("myCanvas");
var cxt=c.getContext("2d");
var i = 0;
var g=cxt.createLinearGradient(0,0,0,c.height);
g.addColorStop(0,"#e0e0e0");
g.addColorStop(1,"#ffffff");
cxt.fillStyle=g;
cxt.fillRect(0,0,c.width,c.height);
var newData = new Array();
for(i=0;i<20;i++)
    newData[i]=i;
var cols=newData.length+1;
var rows=4;
var cell_width=c.width/cols;
var cell_height=c.height/rows;
cxt.strokeStyle="#a0a0a0";
for(i=0;i<=rows;i++)
{
            
            var heiy=cell_height*i;
            cxt.moveTo(0,heiy);
            cxt.lineTo(c.width,heiy);
    }

for(var j=0;j<=cols;j++)
{
           
            var widx=cell_width*j;
            cxt.moveTo(widx,0);
            cxt.lineTo(widx,c.height);
  }
cxt.stroke();
var max_val=0;
 for(i=0;i<newData.length;i++)
 {
       if(max_val<newData[i])
           max_val=newData[i];
   }
 max_val=max_val*1.1;
var points=new Array();
        for(var i=0;i<newData.length;i++)
        {
            var v=newData[i];
            var px=cell_width*(i+1);
            var py=c.height-c.height*(v/max_val);
            points.push({"x":px,"y":py});
        }

cxt.beginPath();
cxt.moveTo(parseInt(points[0].x),parseInt(points[0].y));
for(var i=0;i<newData.length;i++)
 cxt.lineTo(parseInt(points[i].x),parseInt(points[i].y));     
        cxt.strokeStyle="#ee0000";
        cxt.stroke();
for(var j in points)
		{
            var p=points[j];
            cxt.beginPath();
            cxt.arc(p.x, p.y,3,0,2*Math.PI);
            cxt.fillStyle="#ee0000";
            cxt.fill();
        }
     
        