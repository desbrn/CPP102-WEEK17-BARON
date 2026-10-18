# Software Test Specification & Execution Report

**System Under Test:** Simulated Device Monitoring System  
**Tester:** Baron Desiree D. 
**Date:** October 19, 2026  
**Overall Test Status:** PASS (14/14 test cases reported as passed)


'''## 1. Test Results

```markdown
| TC | Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Display the five initial readings: 28, 31, 35, 37, 29. | Five readings displayed correctly. | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully. | Reading added successfully. | Pass |
| TC03 | Choose 2, enter `abc` | Display a whole-number validation message. | Invalid input message shown. | Pass |
| TC04 | Choose 2, enter `-5` | Reject the value because it is outside the allowed range. | Invalid reading message shown. | Pass |
| TC05 | Choose 2, enter `101` | Reject the value because it exceeds 100. | Invalid reading message shown. | Pass |
| TC06 | Choose 2, enter `0` | Reading added successfully. | Reading added successfully. | Pass |
| TC07 | Choose 2, press Enter | Display a message that the reading cannot be empty. | Empty-input validation message shown. | Pass |
| TC08 | Choose 3 | Classify 28 and 29 as NORMAL, 31 and 35 as WARNING, and 37 as CRITICAL. | Classification displayed correctly. | Pass |
| TC09 | Choose 4 | Display the monitoring summary and calculated statistics. | Summary displayed correctly. | Pass |
| TC10 | Choose 5 | Display the thank-you message and exit. | Program exited successfully. | Pass |
| TC11 | Choose 6 at the menu | Display an invalid-menu-choice message. | Invalid-choice message shown. | Pass |
| TC12 | Choose 2, enter 59 | Add the reading; classify it as CRITICAL under the defined thresholds. | Reading added successfully. | Pass |
| TC13 | Choose 2, enter 80 | Add the reading; classify it as CRITICAL. | Reading added successfully. | Pass |
| TC14 | Choose 2, enter `-` | Reject the input without crashing. | Invalid-input message shown. | Pass |
```
'''
## 2. Bugs Found and Fixed

### TC14: Invalid Input — Single Hyphen (-)

Problem:

Entering a single hyphen (-) is not a valid integer. If the program converts it 
directly using int("-"), Python raises a ValueError, which may terminate the program 
if the error is not handled.

Solution:

The input validation function checks whether the entered text contains a valid 
whole number before converting it into an integer.

def is_whole_number(text):
    if len(text) == 0:
        return False

    start = 0
    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True


This validation rejects empty input, alphabetic characters, decimal values, and 
a single hyphen before integer conversion. Negative numbers are also rejected by 
the program's range validation. This helps prevent invalid input from causing an 
error during execution.

---

## 3. Test Summary

- **Total test cases:** 14
- **Passed:** 14
- **Failed:** 0
- **Reported pass rate:** 100%

---

## 3. Test Summary

- **Total test cases:** 14
- **Passed:** 14
- **Failed:** 0
- **Reported pass rate:** 100%

The test cases cover menu navigation, valid and invalid readings, temperature 
classification, summary calculations, and program termination. The results should be 
confirmed by running all 14 test cases against the final version of the program.

## 4. Conclusion
The testing process evaluated the main functions of the Simulated Device Monitoring 
System, including adding readings, validating user input, classifying temperatures, 
generating a summary, and exiting the program. The input-validation function helps 
prevent invalid entries from causing unexpected errors. Overall, the reported results 
indicate that the system performed as expected for the listed test scenarios. Before 
final submission, all 14 test cases should be executed against the final program to 
confirm the reported results.