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
	apn1 - airplane

	(:private
		cit4 - city
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
	(at apn1 apt1)
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
