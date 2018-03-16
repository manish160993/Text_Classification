import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.*;
import java.util.*;

class Import{
		HashSet<String> importWordCount(String s1){
		HashSet<String> h=new HashSet<String>();
		try{
			File folder = new File(s1);
			File[] listOfFiles = folder.listFiles();

			for (File file : listOfFiles) {
				if (file.isFile()) {
				//System.out.println(file.getName());
					BufferedReader br = new BufferedReader(new FileReader(file));
					String st;
					while ((st = br.readLine()) != null)
						{
							String[] s=st.split(" ");
							for(int i=0;i<s.length;i++)
								h.add(s[i]);
						}
				}
			}
		}
		catch(Exception e){
			System.out.println(e);
		}
		return h;
	}
	ArrayList<String> importWordCount1(String s1){
		ArrayList<String> h=new ArrayList<String>();
		try{
			File folder = new File(s1);
			File[] listOfFiles = folder.listFiles();

			for (File file : listOfFiles) {
				if (file.isFile()) {
				//System.out.println(file.getName());
					BufferedReader br = new BufferedReader(new FileReader(file));
					String st;
					String s="";
					while ((st = br.readLine())!= null)
						{
								s+=" "+st;
						}
						h.add(s);
				}
			}
		}
		catch(Exception e){
			System.out.println(e);
		}
		return h;
		
	}
	
	
		HashMap<String,Double> calculateWeights(HashMap<String,Double> vocab1, ArrayList<String> ham,ArrayList<String> spam){
		
		try{
			int z1=ham.size();
			int z2=spam.size();
			int z3=1;
			double n=.6;
			System.out.println(z1+" "+z2);
			while(z3<z1||z3<z2){
					//System.out.println(z3);
					String st;
					if(z3<z1)
					{
						HashMap<String,Double> h=new HashMap<String,Double>();
						double sum=0;
						double t=1;
						double o;
						st=ham.get(z3);
						String[] s=st.split(" ");
						for(int i=0;i<s.length;i++)
							h.put(s[i],(double)h.getOrDefault(s[i],(double)0)+1);
						
						for (Map.Entry<String, Double> entry : vocab1.entrySet()) {
							h.put(entry.getKey(),(double)h.getOrDefault(entry.getKey(),(double)0));
						}
						for (Map.Entry<String, Double> entry : vocab1.entrySet()) {
							if(entry.getKey()!="Rajendra"){
							sum+=vocab1.get(entry.getKey())*h.get(entry.getKey());
							}
						}
						sum+=vocab1.get("Rajendra");
						
						if(sum>=0)
							o=1;
						else
							o=-1;
						double ans=n*(t-o);
						//System.out.println(ans);
						
						for (Map.Entry<String, Double> entry : vocab1.entrySet()) {
							if(entry.getKey()!="Rajendra"){
							vocab1.put(entry.getKey(),vocab1.get(entry.getKey())+ans*h.get(entry.getKey()));
							}
							
						}
						vocab1.put("Rajendra",vocab1.get("Rajendra")+ans);
					
					}
					if(z3<z2)
					{
						HashMap<String,Double> h=new HashMap<String,Double>();
						double sum=0;
						double t=-1;
						double o;
						st=spam.get(z3);
						String[] s=st.split(" ");
						for(int i=0;i<s.length;i++)
							h.put(s[i],(double)h.getOrDefault(s[i],(double)0)+1);
						
						for (Map.Entry<String, Double> entry : vocab1.entrySet()) {
							h.put(entry.getKey(),(double)h.getOrDefault(entry.getKey(),(double)0));
						}
						for (Map.Entry<String, Double> entry : vocab1.entrySet()) {
							if(entry.getKey()!="Rajendra"){
							sum+=vocab1.get(entry.getKey())*h.get(entry.getKey());
							}
						}
						sum+=vocab1.get("Rajendra");
						
						if(sum>=0)
							o=1;
						else
							o=-1;
						double ans=n*(t-o);
						//System.out.println(ans);
						for (Map.Entry<String, Double> entry : vocab1.entrySet()) {
							if(entry.getKey()!="Rajendra"){
							vocab1.put(entry.getKey(),vocab1.get(entry.getKey())+ans*h.get(entry.getKey()));
							}
							
						}
						vocab1.put("Rajendra",vocab1.get("Rajendra")+ans*1);
					
					}
					z3++;
			}
			
		}
		catch(Exception e){
			System.out.println(e);
		}
		return vocab1;
	}
	
	
	
}