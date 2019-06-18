(define (problem probLOGISTICS-7-0) (:domain logistics)
(:objects
	obj21 - package
	obj22 - package
	obj23 - package
	obj33 - package
	obj32 - package
	obj31 - package
	apt3 - airport
	apt2 - airport
	apt1 - airport
	obj11 - package
	obj13 - package
	obj12 - package
	pos2 - location
	pos1 - location
	tru1 - truck
	tru3 - truck
	pos3 - location
	apn1 - airplane
	tru2 - truck

	(:private
		cit3 - city
	)
)
(:init
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(at tru3 pos3)
	(at obj31 pos3)
	(at obj32 pos3)
	(at obj33 pos3)
	(in-city tru3 pos3 cit3)
	(in-city tru3 apt3 cit3)
	(at tru1 pos1)
	(at apn1 apt1)
	(at tru2 pos2)
)
(:goal
	(and
		(at obj22 pos2)
		(at obj33 apt1)
		(at obj12 pos2)
		(at obj13 apt3)
		(at obj31 apt2)
		(at obj23 apt1)
		(at obj32 pos1)
	)
)
)
