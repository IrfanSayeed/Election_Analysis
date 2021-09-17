# **Election_Analysis**

## **Project Overview**

A Colorado Board of Elections employee has given you the following task to complete the election audit of the recent local congressional election.

### Purpose The data requiring retrieval to automate the following:

1. Calculate the total number of votes cast
2. Using a csv file of data, obtain a complete list of candidates and counties receiving votes
3. Calculate the percentage of votes each candidate won and each county won
4. Calculate the total number of votes each candidate won and each county won
5. Determine the winner of the election based on popular vote and the county with the largest voter turnout


## **Resources**
Data Source: election_results.csv -Software: Python 3.7, Visual Studio Code Version: 1.60.0

## **Election-Audit Results** 

The analysis of the election showed that: 

   -**Total votes cast** in the congressional election was **369,711**

  - Vote breakdown of each county in the precinct is as follows: 
    - Jefferson with 38,855 votes representing 10.5% of votes cast 
    - Denver with 306,055 votes representing 82.8% of the votes cast 
    - Arapahoe with 24,801 vote representing 6.7% of the votes cast 
    
 - The county of **Denver has the largest voter turnout** 
 
 - 3 candidates rans in the election 
      - Charles Casper Stockham with 85,213 votes representing 23.0% of the total votes cast 
      - Diana DeGette with 272,892 votes representing 73.8% of the total votes cast 
      - Raymon Anthony Doane with 11,606 votes representing 3.1% of the total votes cast 
      
  - The **winner of the election was Diana DeGette**, winning with 272,892 votes representing 73.8% of the total votes cast

## **Election-Audit Summary:**
It is proposed that the election commission modify the current script for use with any election. The code would be simplified and easier to read.

Current script can be modified by initiating the following code changes:

### Recommendation 1

- Currently the script is very long, difficult to read and has a multitude of variables to track within several For and If statments
propose consolidating candidate specifc and county specific variables.
- Example: rather than tracking "winning candidate" and "winning county separately", combine to track "winning_candidate_county".
- This will result a lower level index, which will reduce the multiple variable names, but reduce the number of for and if statements currently in the script.  It will simplify some of the calculations, ie. the use of the total vote count for all the percentages for candidate and counties


### Recommendation 2

- Consolidate the print commands for candidates and counties into 1 statement.
- Current code has print commands for county and candidate data within 4 sections of code creating a consolidated output in the Election_Analysis text file

output request to terminal and text file in Analysis:

<img width="411" alt="PrintOutput" src="https://user-images.githubusercontent.com/89538802/133714375-2edf38f1-30f0-44b7-9322-6166c48bf591.PNG">


