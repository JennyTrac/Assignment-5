/* Created by Jenny Trac
Created on Nov 4 2017
Program lets user play a simplied version of Blackjack against the computer */

import java.util.Scanner;
import java.util.Random;

public class GameOf21 {
  
    public static void main(String[] args)
    {
    // constants and variables
    Random rand = new Random();
    final int MAXCARDVALUE = 10 + 1;
    final int MINCARDVALUE = 1;
    int usercard1 = rand.nextInt(MAXCARDVALUE - MINCARDVALUE) + MINCARDVALUE;
    int usercard2 = rand.nextInt(MAXCARDVALUE - MINCARDVALUE) + MINCARDVALUE;
    int usercard3 = 0; //!!!!!!!????
    int usertotal = usercard1 + usercard2 + usercard3; //!!!!!!!????
    int dealercard1 = rand.nextInt(MAXCARDVALUE - MINCARDVALUE) + MINCARDVALUE;
    int dealercard2 = rand.nextInt(MAXCARDVALUE - MINCARDVALUE) + MINCARDVALUE;
    int dealercard3 = rand.nextInt(MAXCARDVALUE - MINCARDVALUE) + MINCARDVALUE;
    int dealertotal = dealercard1 + dealercard2 + dealercard3;
    
    // instructions
    System.out.println("Card values range from 1 - 10.");
    System.out.println("The dealer is dealt 3 cards and you are dealt 2.");
    System.out.println("The goal is to get as close to the value of 21 as possible without going over.");
    System.out.println("Your cards are: " +  usercard1 + ", " + usercard2);
    System.out.println("Your total is: " + usertotal);
    System.out.println("If you would like another card, enter: 1.");
    System.out.println("If you are happy with your cards, enter 2.");
    
    // input
    Scanner problem = new Scanner(System.in);
        int user_input = (problem.nextInt());
     
     // process
     if ((user_input == 1) || (user_input == 2))
         {
         if (user_input == 1)
             {
             usercard3 = rand.nextInt(MAXCARDVALUE - MINCARDVALUE) + MINCARDVALUE;  //?!?!?!?!
             System.out.println("Your cards are: " + usercard1 + ", " + usercard2 + ", " + usercard3);
             }
         else if (user_input == 2)
             {
             usercard3 = 0; //?!?!?!?!
             }
         usertotal = usercard1 + usercard2 + usercard3; 
         System.out.println("Your total is: " + usertotal);
         System.out.println("The dealer's cards are: " + dealercard1 + ", " + dealercard2 + ", " + dealercard3);
         System.out.println("The dealer's total is: " + dealertotal);
         
         // output
         if ((usertotal == dealertotal) || (usertotal > 21 && dealertotal >21))
             {
             System.out.println("You tied.");
             }
         else if ((dealertotal <= 21 && usertotal > 21) || ((usertotal < dealertotal)&&(dealertotal <=21)))
             {
             System.out.println("You lose.");
             }
         else
             {
             System.out.println("You win.");
             }
         }

     else
         {
         System.out.println("Not an option.");
         } 
    
    }

}
