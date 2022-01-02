import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

class Caculator_Citys {
    public static void main(String[] args) {
        Dataset<Row> result;

        /**
         * 计算全国多个城市的平均房价（元/平方米）
         * 将结果写入集合avg_city
         */
        MongoDBSparkConn conn = new MongoDBSparkConn("crawl_beike", "AllCitysData");
        String statement = "select city, sum(price_perSQM*area)/sum(area) from table " +
                            "group by city";
        result = conn.query(statement);
        conn.save(result, "avg_city");

    }
}
