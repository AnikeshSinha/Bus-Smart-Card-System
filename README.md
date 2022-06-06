# Bus-Smart-Card-System

**Problem Statement :**

Implement an automated Bus Smart Card System for a small town. The town has a
single road that connects both end of the town.

**High level Requirements:**

  1) There is a single bus route number 108 that have 15 bus stops. The stops name
  are Stop1,Stop2,Stop3,…Stop15.
  
  2) The travel can be in any direction from any stop except Stop1 and Stop15. On
  Stop1 and Stop15 travellers can only travel in one direction.
  
  3) Travellers have smart card that behave just like any other regular debit card that
  has an initial balance when purchased. Travellers swipe in when they enter a bus
  and swipe out when they exit. Card balance is automatically updated at swipe
  out.
  
  4) Smart Card should have a minimum balance of 10 dollars at swipe-in.

  5) At swipe-out, system should calculate the fare based on below strategies. The
  fare must be deducted from the card. Card should have the sufficient balance
  otherwise user should not be able to exit.
  
      • Night time (23:00 - 6:00 swipe-in time) - 60 cents * (Number of stops travelled)
      
      • Day time (6:00 - 23:00 swipe-in time) - 80 cents * (Number of stops traveled)
      
      • If number of stations travelled is more than 5 then give 20% long distance
      discount for travel beyond 5 stops. The discount will be on number of stops
      beyond 5 and not for initial 5 stops.
      
      • Give 10% Weekend discount on Saturdays and Sundays.
      
      •Max fare can be 10 dollars
