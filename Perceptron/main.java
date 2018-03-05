import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.io.*;


public class main{
	
	
	public static void main(String[] arg) {

	Scanner scan=new Scanner(System.in);
	
	
		try{
			HashMap<String> vocab=new HashMap<String>();
			HashMap<String,Integer> ham=new HashMap<String,Integer>();
			HashMap<String,Integer> spam=new HashMap<String,Integer>();
			int noOfSpam=0;int noOfHam=0;
			Constant.ham=scan.nextLine().trim(); 
			Constant.spam=scan.nextLine().trim();
			String y=scan.nextLine().trim();
			Constant.test="C:/Users/manis/Desktop/Github/Text_Classification/Naive/enron1/test/"+y;
			Import im=new Import();
			
			ham=im.importWordCount(Constant.ham); //HashMap with Ham words and their count
			
			spam=im.importWordCount(Constant.spam); //HashMap with Spam words and their count
			
			vocab=im.importWords(ham,vocab);
			//System.out.println(vocab.size()+" "+ham.size());
			vocab=im.importWords(spam,vocab);
			//System.out.println(vocab.size()+" "+spam.size());

			
		}
		catch(Exception e){
			System.out.println(e);
		}
	
	}
}