(define (problem probLOGISTICS-4-0) (:domain logistics)
(:objects
	obj21 - package
	obj22 - package
	obj23 - package
	apt2 - airport
	apt1 - airport
	obj11 - package
	obj13 - package
	obj12 - package
	pos1 - location
	pos2 - location
	cit2 - city
	tru2 - truck
	apn1 - airplane
	cit1 - city
	tru1 - truck

	(:private
	)
)
(:init
	(at apn1 apt2)
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(at tru2 pos2)
	(in-city tru2 pos2)
	(in-city tru2 apt2)
	(at tru1 pos1)
	(in-city tru1 pos1)
	(in-city tru1 apt1)
)
(:goal
	(and
		(at obj11 apt1)
		(at obj23 pos1)
		(at obj13 apt1)
		(at obj21 pos1)
	)
)
)
