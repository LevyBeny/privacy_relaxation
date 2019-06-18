(define (problem probLOGISTICS-15-0) (:domain logistics)
(:objects
	obj41 - package
	apt3 - airport
	apt2 - airport
	apt1 - airport
	apt5 - airport
	apt4 - airport
	pos4 - location
	pos5 - location
	pos2 - location
	pos3 - location
	obj21 - package
	obj22 - package
	obj23 - package
	obj33 - package
	obj32 - package
	obj31 - package
	obj42 - package
	obj43 - package
	obj53 - package
	obj52 - package
	obj11 - package
	obj51 - package
	obj13 - package
	obj12 - package
	pos1 - location
	apn1 - airplane
	apn2 - airplane
	tru1 - truck
	cit1 - city
	tru2 - truck
	cit2 - city
	tru3 - truck
	cit3 - city
	tru4 - truck
	cit4 - city
	tru5 - truck
	cit5 - city

	(:private
	)
)
(:init
	(at tru1 pos1)
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(at obj31 pos3)
	(at obj32 pos3)
	(at obj33 pos3)
	(at obj41 pos4)
	(at obj42 pos4)
	(at obj43 pos4)
	(at obj51 pos5)
	(at obj52 pos5)
	(at obj53 pos5)
	(in-city tru1 pos1 cit1)
	(in-city tru1 apt1 cit1)
	(at apn1 apt5)
	(at apn2 apt2)
	(at tru2 pos2)
	(in-city tru2 pos2 cit2)
	(in-city tru2 apt2 cit2)
	(at tru3 pos3)
	(in-city tru3 pos3 cit3)
	(in-city tru3 apt3 cit3)
	(at tru4 pos4)
	(in-city tru4 pos4 cit4)
	(in-city tru4 apt4 cit4)
	(at tru5 pos5)
	(in-city tru5 pos5 cit5)
	(in-city tru5 apt5 cit5)
)
(:goal
	(and
		(at obj22 apt4)
		(at obj31 apt4)
		(at obj43 pos5)
		(at obj13 apt1)
		(at obj23 pos4)
		(at obj12 pos2)
		(at obj51 pos3)
		(at obj32 pos3)
		(at obj11 apt3)
		(at obj42 apt2)
		(at obj52 apt4)
		(at obj33 apt3)
		(at obj21 pos3)
		(at obj53 apt2)
		(at obj41 apt1)
	)
)
)
