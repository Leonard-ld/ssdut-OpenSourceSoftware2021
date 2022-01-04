import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

public class Area_Distrabution {
    public static void main(String[] args) {
        Dataset<Row> result;
        /**
         * 计算北京各个区的平均房价（元/平方米）
         * 将结果写入集合beijing_avg_area
         */
        MongoDBSparkConn conn = new MongoDBSparkConn("crawl_beike", "AllCityData");
        String statement = "select  " +
                "    case  " +
                "      when area < 30 then '20-30'  " +
                "      when area >= 30 and area < 40  then '30-40' " +
                "      when area >= 40 and area < 50  then '40-50' " +
                "      when area >= 50 and area < 60  then '50-60' " +
                "      when area >= 60 and area < 70  then '60-70' " +
                "      when area >= 70 and area < 80  then '70-80' " +
                "      when area >= 80 and area < 90  then '80-90' " +
                "      when area >= 90 and area < 100  then '90-100' " +
                "      when area >= 100 and area < 110  then '100-110' " +
                "      when area >= 110 and area < 120  then '110-120' " +
                "      when area >= 120 and area < 130  then '120-130' " +
                "      when area >= 130 and area < 140  then '130-140' " +
                "      when area >= 140 and area < 150  then '140-150' " +
                "      when area >= 150 and area < 160  then '150-160' " +
                "      when area >= 160 and area < 170  then '160-170' " +
                "      when area >= 170 and area < 180  then '170-180' " +
                "      when area >= 180 and area < 190  then '180-190' " +
                "      when area >= 190 and area < 200  then '190-200' " +
                "      when area >= 200 and area < 210  then '200-210' " +
                "      when area >= 210 and area < 220  then '210-220' " +
                "      when area > 220 then '220+' " +
                "    end  " +
                "    as name,  " +
                "    count(*) as num " +
                "from table c " +
                "group by name";
        result = conn.query(statement);
        conn.save(result, "area_distrabution");


    }
}
