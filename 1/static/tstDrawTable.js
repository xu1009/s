//得到画布
    var can1=document.getElementById("myCanvas");
    //得到画笔
    var cxt=can1.getContext("2d");

    //定义图表的数据，该方式为创建数组直接量的方式
    var sale_data=[80,92,104,110,68,50,45,90,74,68,98,103];

    //首先为背景进行设置渐变的效果,表示的是从(0,0)到(600,0)即纵坐标上边显示渐变的效果
    var g=cxt.createLinearGradient(0,0,0,100);
    g.addColorStop(0,"#e0e0e0");
    g.addColorStop(1,"#ffffff");
    //将渐变效果添加在我们的画布上边
    cxt.fillStyle=g;
    //开始绘制效果
    cxt.fillRect(0,0,can1.width,can1.height);

    //设置要绘制方格的行数和列数
    var cols=sale_data.length+1;
    var rows=4;

    //计算每一个小方格的宽度和高度
    var cell_width=can1.width/cols;
    var cell_height=can1.height/rows;

    //设置绘制的颜色
    cxt.strokeStyle="#a0a0a0";
    //调用绘制表格的函数
    drawTable(sale_data);

    //绘制表格的函数
    function drawTable(data){
        cxt.beginPath();
        //开始画竖线
        for(var i=0;i<=rows;i++){
            //计算绘制的坐标
            var heiy=cell_height*i;
            cxt.moveTo(0,heiy);
            cxt.lineTo(can.width,heiy);
        }

        //绘制横线
        for(var j=0;j<=cols;j++){
            //计算绘制的坐标
            var widx=cell_width*j;
            cxt.moveTo(widx,0);
            cxt.lineTo(widx,can1.height);
        }

        //绘制表格完成
        cxt.stroke();

        //获取数据当中的最大值，以便可以划分纵坐标轴，来进行绘图，即每个像素代表的数值是多少，纵坐标的最大值
        var max_val=0;
        for(var i=0;i
            if(max_val
                max_val=data[i];
            }
        }
        //之后我们对最大值再放大一点，作为坐标轴的最大值
        max_val=max_val*1.1;

        //现在我们计算每个数据的坐标轴
        //这里我们将计算出来的坐标轴数据写入到我们的数组对象当中去
        var points=[];
        for(var i=0;i
            var v=data[i];
            var px=cell_width*(i+1);
            var py=can1.height-can1.height*(v/max_val);
            points.push({"x":px,"y":py});
        }

        //开始绘制折线
        cxt.beginPath();
        cxt.moveTo(points[0].x,points[0].y);
        for(var j=1;j
            cxt.lineTo(points[j].x,points[j].y);
        }
        cxt.strokeStyle="#ee0000";
        cxt.stroke();

        //绘制坐标的小圆点
        for(var j in points){
            var p=points[j];
            cxt.beginPath();
            cxt.arc(p.x, p.y,6,0,2*Math.PI);
            cxt.fillStyle="#ee0000";
            cxt.fill();
        }
    }