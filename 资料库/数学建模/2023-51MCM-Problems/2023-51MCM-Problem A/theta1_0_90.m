clc

clear all

g=9.8;

m=5;

C=0.5;
t=0;
r=0.08;

A=pi*r^2;

rou=1.24;

D=(rou*C*A)/2;
for the=1:8
    t=0;
    detat=0.01;
    fd(the,1)=0;
    fx(the,1)=0;
    fy(the,1)=0;
    %theta=(-35/180*pi);
    theta=-the*10/180*pi;
    x(1)=0;
    
    y(1)=0;
    d(1)=0;
    
    V(1)=900/3.6+6;
    
    Vx(1)=V(1)*cos(theta);
    
    Vy(1)=V(1)*sin(theta);
    
    N=1000;
    
    for n=1:N
    
    V(n)=sqrt(Vx(n)^2+Vy(n)^2)
    ax(n)=-(D/m)*V(n)*Vx(n);
    
    ay(n)=-g-(D/m)*V(n)*Vy(n);
    
    Vx(n+1)=Vx(n)+ax(n)*detat;
    
    Vy(n+1)=Vy(n)+ay(n)*detat;
    
    x(n+1)=x(n)+Vx(n)*detat+0.5*ax(n)*detat^2; 
    y(n+1)=y(n)+Vy(n)*detat+0.5*ay(n)*detat^2; 
    d(n)=sqrt(x(n)^2+y(n)^2);
    
    
    if y(n)<=-300 && y(n)>=-800 &&d(n)>=1000 && d(n)<=3000
         t=t+1;
         fd(the,t)=d(n);
         fx(the,t)=x(n);
         fy(the,t)=y(n);
        
    end
    %if y(n+1)<=-300 
       
    %   break
    %end    
    
    px(n)=Vx(1)*n*detat;
    py(n)=Vy(1)*n*detat-0.5*g*(n*detat)^2; 
    end
    
    plot(x,y,'r',px,py,'g');
    
    grid
    
    xlabel('x'),ylabel('y');
    
    title('有空气阻力的抛射体运动')
end