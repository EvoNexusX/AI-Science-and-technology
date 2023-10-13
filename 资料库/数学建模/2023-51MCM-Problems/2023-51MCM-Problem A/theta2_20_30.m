clc

clear all

g=10;

m=5;

C=0.4;
t=0;
r=0.08;

A=pi*r^2;
aa(1)=1;
rou=1.29;
tt(1)=0;
D=(rou*C*A)/2;
thes(1)=0;
for the=1:10
    t=1;  
    detat=0.01;
    fd(the,1)=0;
    fx(the,1)=0;
    fy(the,1)=0;
    pd(the,1)=0;
    %theta=(-35/180*pi);
    %theta=23.5/180*pi;
    %theta=1/20*pi;
    theta=(the*5)/180*pi;
    thes(the)=theta;
    x(1)=0;
    
    y(1)=0;
    d(1)=0;
    vf=0;% 风
    V(1)=900/3.6;
    Vx(the,1)=V(1)*cos(theta);
    
    Vy(the,1)=V(1)*sin(theta);
    
    N=1000;
    
    for n=1:N
    
    V(n)=sqrt(Vx(the,n)^2+Vy(the,n)^2)
    ax(n)=-(D/m)*(Vx(the,n)-vf*cos(theta))*(Vx(the,n)-vf*cos(theta));
    if n>1 && Vy(the,n)==Vy(the,n-1)
        ay(n)=0; 
    else
        ay(n)=g-(D/m)*(Vy(the,n)-vf*sin(theta))*(Vy(the,n)-vf*sin(theta));
    end
    Vx(the,n+1)=Vx(the,n)+ax(n)*detat;
    if Vx(the,n+1)<0
        Vx(the,n+1)=Vx(the,n);
    end
    eps=0.03;
    aa(n)=ay(n);
    if (-eps<=ay(n) && ay(n)<=eps)
        Vy(the,n+1)=Vy(the,n);
        x(n+1)=x(n)+Vx(the,n)*detat;
        y(n+1)=y(n)+Vy(the,n)*detat;
    else
        Vy(the,n+1)=Vy(the,n)+ay(n)*detat; 
        x(n+1)=x(n)+Vx(the,n)*detat+0.5*ax(n)*detat^2; 
        y(n+1)=y(n)+Vy(the,n)*detat+0.5*ay(n)*detat^2; 
    end
   
    d(n)=sqrt(x(n)^2+y(n)^2);
    
    t=t+1;
    tt(the,t)=n*detat;
    if y(n)>=300 && y(n)<=800 &&d(n)>=1000 && d(n)<=3000
         
         fd(the,n)=d(n);
         fx(the,n)=x(n);
         fy(the,n)=y(n);
         
    
        
    end
    %if y(n+1)<=-300 
       
    %   break
    %end    
    
    px(n)=Vx(the,1)*n*detat;
    py(n)=Vy(the,1)*n*detat+0.5*g*(n*detat)^2; 
    pd(n)=sqrt(px(n)^2+py(n)^2);
    end
    
    plot(x,y,'r',px,py,'g');
    
    grid
    
    xlabel('x'),ylabel('y');
    
    title('有空气阻力的抛射体运动')
end