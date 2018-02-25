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
			HashSet<String> vocab=new HashSet<String>();
			HashMap<String,Integer> ham=new HashMap<String,Integer>();
			HashMap<String,Integer> spam=new HashMap<String,Integer>();
			int noOfSpam=0;int noOfHam=0;
			Constant.ham=scan.nextLine().trim(); 
			Constant.spam=scan.nextLine().trim();
			String y=scan.nextLine().trim();
			Constant.test="C:/Users/manis/Desktop/Study/2nd_sem/ML/Assign 2/enron4/train/"+y;
			Import im=new Import();
			
			
			
			ham=im.importWordCount(Constant.ham); //HashMap with Ham words and their count
			
			spam=im.importWordCount(Constant.spam); //HashMap with Spam words and their count
			
			 noOfHam=im.importNoOfDocs(Constant.ham);
			 noOfSpam=im.importNoOfDocs(Constant.spam);
			double proHam=(double)noOfHam/(noOfHam+noOfSpam);
			double proSpam=(double)noOfSpam/(noOfHam+noOfSpam);
			
			vocab=im.importWords(ham,vocab);
			//System.out.println(vocab.size()+" "+ham.size());
			vocab=im.importWords(spam,vocab);
			//System.out.println(vocab.size()+" "+spam.size());
			
			HashMap<String,Double> ansHam=new HashMap<String,Double>();
			ansHam=im.calculateConditional(vocab,ham);
			HashMap<String,Double> ansSpam=new HashMap<String,Double>();
			ansSpam=im.calculateConditional(vocab,spam);
			int total=0;
			int totalDocs=0;
			//System.out.println(ansHam+" "+ansSpam);
			File folder = new File(Constant.test);
			File[] listOfFiles = folder.listFiles();
			double accuracy=0;
			for (File file : listOfFiles) {
			if (file.isFile()) {
			HashMap<String,Double> testHam=new HashMap<String,Double>();
			BufferedReader br = new BufferedReader(new FileReader(file));
			totalDocs++;
			double scoreHam=0;
			scoreHam=Math.log(proHam);
			//System.out.println(proHam);
			String st;
			while ((st = br.readLine()) != null)
			{
				String[] s=st.split(" ");
				for(int i=0;i<s.length;i++)
				{testHam.put(s[i],ansHam.getOrDefault(s[i],(double)1/ansHam.size()));
				scoreHam+=Math.log(testHam.get(s[i]));
				//System.out.println(s[i]+" "+testHam.get(s[i]));
				}
			}
			HashMap<String,Double> testSpam=new HashMap<String,Double>();
			br = new BufferedReader(new FileReader(file));
 
			double scoreSpam=0;
			scoreSpam=Math.log(proSpam);
			
			while ((st = br.readLine()) != null)
			{
				String[] s=st.split(" ");
				for(int i=0;i<s.length;i++)
				{testSpam.put(s[i],ansSpam.getOrDefault(s[i],(double)1/ansSpam.size()));
				scoreSpam+=Math.log(testSpam.get(s[i]));}
			}
			if(scoreHam>=scoreSpam)
				total++;
			}
			
			if(y.equals("spam"))
				accuracy=(double)(totalDocs-total)/totalDocs;
			else
				accuracy=((double)total/totalDocs);
			}
			
			
			System.out.println(accuracy);
			
		}
		catch(Exception e){
			System.out.println(e);
		}
	
	}
}