Get Function 1
collects all the fruit data once it is available and not removed through placing it into a new list called fruits available 

Get Function 2 
gets specific fruit data once the id is affixed to the search, if it is not there it will say fruit is not found 

Post Function 
posts the new fruit information created by the user and the creation date is not created by the user but the actual system. If the requirements in terms of fields needed, are not met it raises an error message to suggest that the client made an error

Patch Function 
Using the fruit update base model, the user is allowed to edit the fields of availability, quantity and price once the corresponding id is found and update the stored data on the fruit in the list accordingly and the status code shows successful update of the fruit information 

Delete Function 
Using the specified ID, the user is able to set the availability of a fruit to false which removes it from the listing once get all fruits function is called since it only pulls on fruits with available for that get function, if id is not seen, the corresponding HTTP code pop up
