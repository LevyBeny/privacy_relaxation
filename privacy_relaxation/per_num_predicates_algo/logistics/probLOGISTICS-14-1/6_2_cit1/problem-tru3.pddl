(define (problem probLOGISTICS-14-1) (:domain logistics)
(:objects
	obj41 - package
	apt3 - airport
	apt2 - airport
	apt1 - airport
	apt5 - airport
	apt4 - airport
	pos4 - location
	pos3 - location
	pos1 - location
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
	pos2 - location
	pos5 - location
	apn1 - airplane
	apn2 - airplane
	tru1 - truck
	cit1 - city

	(:private
		tru3 - truck
		cit3 - city
	)
)
(:init
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at tru3 pos3)
	(at obj31 pos3)
	(at obj32 pos3)
	(at obj33 pos3)
	(at obj41 pos4)
	(at obj42 pos4)
	(at obj43 pos4)
	(in-city tru3 pos3 cit3)
	(in-city tru3 apt3 cit3)
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(at obj51 pos5)
	(at obj52 pos5)
	(at obj53 pos5)
	(at apn1 apt1)
	(at apn2 apt5)
	(at tru1 pos1)
	(in-city tru1 pos1 cit1)
	(in-city tru1 apt1 cit1)
)
(:goal
	(and
		(at obj33 pos3)
		(at obj22 pos3)
		(at obj13 apt2)
		(at obj43 apt1)
		(at obj41 apt1)
		(at obj51 pos4)
		(at obj53 apt5)
		(at obj11 pos4)
		(at obj31 pos3)
		(at obj42 pos1)
		(at obj52 pos1)
		(at obj12 apt3)
		(at obj32 apt4)
		(at obj21 pos4)
	)
)
)
