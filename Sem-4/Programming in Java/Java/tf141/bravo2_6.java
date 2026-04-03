

class bravo2_6{
    String name;
    int age;
    String rank;

    //constructor
    bravo2_6(String name,int age,String rank){
        this.name=name;
        this.age=age;
        this.rank=rank;
    }

    void deploy__bravo(){
        System.out.println(" Name : ");
        System.out.println(" Age  : ");
        System.out.println(" Rank : ");
    };
    void standby__bravo(){
        System.out.println(name+":  Bravo 2-6 standing by...Come in Viper");
    };
    void VIPER__to__bravo2_6(){
        System.out.println("Viper  : Sending Exfil ETA 7 mikes."+"Sergeant "+name +" ,Site too hot,too many hostiles on the roof top. clear the evac site asap. Viper out.");
    };
    void sitrep(){
        System.out.println(name+"Bravo2_6 to Viper; Hostiles eliminated. LZ is clear.Take your time VIPER. Bravo2_6 out.");
    };


    public static void main(String[] args) {
        bravo2_6 id___1 = new bravo2_6("Alex mason", 48,"Sergeant");
        id___1.deploy__bravo();
        id___1.standby__bravo();
        id___1.VIPER__to__bravo2_6();
        id___1.sitrep();
        
    }
    

}