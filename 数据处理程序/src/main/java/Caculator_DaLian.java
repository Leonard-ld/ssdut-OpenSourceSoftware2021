import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

class Caculator_DaLian {
    public static void main(String[] args) {
        Dataset<Row> result;
        /**
         * 计算大连各个区的平均房价（元/平方米）
         * 将结果写入集合dalian_avg_area
         */
        MongoDBSparkConn conn = new MongoDBSparkConn("crawl_beike", "dalian");
        String statement = "select avg(price_perSQM), area_name from table"+
                            " group by area_name";
        result = conn.query(statement);
        conn.save(result, "dalian_avg_area");
    }
}
