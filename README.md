Project Description

This Python program accepts package weights, categorizes them into different load types, applies personalization logic based on the user's full name and destination, and generates a final loading report.

Personalization Logic

Personalization in this program is based on:

Full Name

L Value (without spaces)

PLI Value

Applied Rule

Destination Safety Check

 Full Name Used

injam venkata gopi harsha vardhan

 L Value (Without Spaces)

L is calculated as the total number of characters in the full name excluding spaces.

Count:

injam → 5

venkata → 7

gopi → 4

harsha → 6

vardhan → 7

Total:

L = 29

 PLI Value

PLI (Personalized Load Index) is calculated using:

PLI = L % 3


So,

PLI = 29 % 3 = 2


PLI Value = 2

 Applied Rule

Applied Rule: Rule C

Under Rule C:

All Very Light loads are removed.

All Overload items are removed.

Only Normal Load, Heavy Load, and Invalid Entries remain in the final loading plan.

 Destination Safety Personalization

The user enters the destination of the load.

The program:

Counts the number of characters in the destination excluding spaces.

Checks whether the count is even or odd.

Safety Rule:

If character count is even → Go Safe

If character count is odd → Drive Safe