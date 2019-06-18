(define (problem probLOGISTICS-12-0) (:domain logistics)
(:objects
	apt3 - airport
	apt2 - airport
	apt1 - airport
	apt4 - airport
	pos4 - location
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
	obj41 - package
	obj11 - package
	obj13 - package
	obj12 - package
	cit1 - city
	cit3 - city
	tru2 - truck
	tru1 - truck
	tru3 - truck
	cit4 - city

	(:private
		pos1 - location
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
	(in-city tru1 pos1 cit1)
	(in-city tru1 apt1 cit1)
	(at tru2 pos2)
	(at tru3 pos3)
	(in-city tru3 pos3 cit3)
	(in-city tru3 apt3 cit3)
)
(:goal
	(and
		(at obj13 apt1)
		(at obj42 pos4)
		(at obj31 pos3)
		(at obj33 pos2)
		(at obj43 pos4)
		(at obj32 apt4)
		(at obj21 apt2)
		(at obj11 apt4)
		(at obj22 pos2)
		(at obj41 apt1)
		(at obj12 apt4)
		(at obj23 pos4)
	)
)
)
