parent(fred,jack).
parent(fred,chae).
parent(fred,kim).
parent(dave,fred).
parent(hanni,park).

gender(fred,male).
gender(dave,male).
gender(jack,male).
gender(kim,male).
gender(lee,male).
gender(chae,female).
gender(hanni,female).
gender(jenny,female).
gender(mary,female).

couple(kim,chae).
couple(lee,hanni).
couple(fred,mary).

% Rules
grandparent(Elder,Younger) :- 
  parent(Elder,P),
  parent(P,Younger).

sibling(A,B) :-
 parent(P,A),
 parent(P,B),
 not(A=B). % you are not your own sibling

father(Dad,Child) :-
    parent(Dad,Child),
    gender(Dad,male).

father(Dad,Child) :-
    parent(Mom,Child),
    couple(Dad,Mom).
    
mother(Mom,Child) :-
    parent(Mom,Child),
    gender(Mom,female).

mother(Mom,Child) :-
    parent(Dad,Child),
    couple(Dad,Mom).
	
    

