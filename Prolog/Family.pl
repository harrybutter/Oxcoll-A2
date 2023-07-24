/* Facts and rules - families example */ 

% Facts - Fred has three children, his father is Dave
parent(fred,jack).
parent(fred,alia).
parent(fred,paul).
parent(dave,fred).

% Rules
grandparent(Elder,Younger) :- 
  parent(Elder,P),
  parent(P,Younger).

sibling(A,B) :-
 parent(P,A),
 parent(P,B),
 not(A=B). % you are not your own sibling
 
 
 % extend by adding facts and rules for father, mother, brother and sister
 
 % Example Queries
 % sibling(jack,X).
 % grandparent(dave,alia).