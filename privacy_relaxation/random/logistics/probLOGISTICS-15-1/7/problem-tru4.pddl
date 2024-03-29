(define (problem probLOGISTICS-15-1) (:domain logistics)
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
	cit1 - city
	cit4 - city
	pos5 - location
	tru2 - truck
	apn1 - airplane
	tru5 - truck
	cit2 - city

	(:private
		tru4 - truck
	)
)
(:init
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at obj31 pos3)
	(at obj32 pos3)
	(at obj33 pos3)
	(at tru4 pos4)
	(at obj41 pos4)
	(at obj42 pos4)
	(at obj43 pos4)
	(in-city tru4 pos4 cit4)
	(in-city tru4 apt4 cit4)
	(at obj51 pos5)
	(at obj52 pos5)
	(at obj53 pos5)
	(at apn1 apt2)
	(at tru5 pos5)
	(in-city tru2 apt2 cit2)
)
(:goal
	(and
		(at obj31 apt4)
		(at obj22 apt2)
		(at obj42 apt4)
		(at obj53 apt3)
		(at obj12 pos1)
		(at obj32 apt1)
		(at obj43 apt3)
		(at obj52 apt1)
		(at obj51 apt3)
		(at obj21 apt4)
		(at obj11 pos3)
		(at obj23 pos4)
		(at obj33 pos3)
		(at obj13 apt3)
		(at obj41 pos1)
	)
)
)
