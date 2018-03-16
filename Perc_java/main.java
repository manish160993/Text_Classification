import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.io.*;
import java.util.Random;


public class main{
	
	
	public static void main(String[] arg) {

	Scanner scan=new Scanner(System.in);
	
	
		try{
			HashSet<String> vocab=new HashSet<String>();
			HashMap<String,Double> vocab1=new HashMap<String,Double>();
			HashSet<String> ham=new HashSet<String>();
			HashSet<String> spam=new HashSet<String>();
			ArrayList<String> hamA=new ArrayList<String>();
			ArrayList<String> spamA=new ArrayList<String>();
			ArrayList<String> hamTest=new ArrayList<String>();
			ArrayList<String> spamTest=new ArrayList<String>();
			Constant.ham=scan.nextLine().trim(); 
			Constant.spam=scan.nextLine().trim();
			Constant.testHam=scan.nextLine().trim();
			Constant.testSpam=scan.nextLine().trim();
			Import im=new Import();
			
			ham=im.importWordCount(Constant.ham); //HashMap with Ham words and their count
			spam=im.importWordCount(Constant.spam);
			System.out.println(ham.size()+" "+spam.size());
			vocab.addAll(ham);
			vocab.addAll(spam);
			Iterator<String> it = vocab.iterator();
			while(it.hasNext()){
				vocab1.put(it.next(),Math.random());
			}
			//System.out.println(vocab1);
			vocab1.put("Rajendra",(double)1);
			
			hamA=im.importWordCount1(Constant.ham);
			spamA=im.importWordCount1(Constant.spam);
			//System.out.println(vocab1);
			for(int i=0;i<25;i++){
			vocab1=im.calculateWeights(vocab1,hamA,spamA);
			//System.out.println(hamA);
			
			}
			hamTest=im.importWordCount1(Constant.testHam);
			spamTest=im.importWordCount1(Constant.testSpam);
			//System.out.println(hamTest+" "+spamTest);
			//System.out.print(vocab1.get("Rajendra")+" "+vocab1.size()+" "+hamTest.size()+" "+spamTest.size());
			int q=0;
			for(int j=1;j<hamTest.size();j++){
			String st=hamTest.get(j);
			String[] s=st.split(" ");
			double sum=0;
			for(int i=0;i<s.length;i++){
				if(vocab1.containsKey(s[i]))
					sum+=vocab1.get(s[i]);
			}
			sum+=vocab1.get("Rajendra");
			//sum+=vocab1.get("Rajendra");
			if(sum>=0)
				q++;
			}
			
			//System.out.println(vocab1);
			//System.out.println(Arrays.toString(weights));
			System.out.println("q "+ q);
			q=0;
			for(int j=1;j<spamTest.size();j++){
			String st=spamTest.get(j);
			String[] s=st.split(" ");
			double sum=0;
			for(int i=0;i<s.length;i++){
				if(vocab1.containsKey(s[i]))
					sum+=vocab1.get(s[i]);
			}
			sum+=vocab1.get("Rajendra");
			if(sum<0)
				q++;
			}
			System.out.println("q "+ q);
			System.out.print(vocab1.get("Rajendra")+" "+vocab1.size()+" "+hamTest.size()+" "+spamTest.size());
			
		}
		catch(Exception e){
			System.out.println(e);
		}
	}
}