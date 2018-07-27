%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%PHYS 423 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc
clear
N = 4;
L = 2*pi;
x = linspace(0,L,N);

dx = x(2)-x(1);

D = (diag(ones((N),1),1)-diag(ones((N),1),-1))/(2*dx);

D(1,2) = 0;
D(2,1) = 0;

D(N,N-1) = 0;
D(N-1,N) = 0;


Lap = (-2*diag(ones(N,1),0)+diag(ones((N-1),1),1)+diag(ones((N-1),1),-1))/(dx^2);
%-2*identity matrix +  off diag + off diag


Lap(1,1) = 0;
Lap(1,2) = 0;
Lap(2,1) = 0;

Lap(N,N-1) = 0;
Lap(N-1,N) = 0;
Lap(N,N) = 0;

e = ones(N,1);
Lap2 = spdiags([e -2*e e],[-1 0 1],N,N)/dx^2;

Lap2(1,1) = 0;
Lap2(1,2) = 0;
Lap2(2,1) = 0;

Lap2(N,N-1) = 0;
Lap2(N-1,N) = 0;
Lap2(N,N) = 0;

%disp(D);
disp(Lap);
disp(Lap2);
