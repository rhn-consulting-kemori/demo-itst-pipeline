package com.redhat.example.entity;

import lombok.Data;
import java.util.List;

// API-POST Data
@Data
public class ApiPostDataEntity {

    /** 名前 */
    private String name;

    /** Url */
    private String url;

    /** Method */
    private String method;

    /** 詳細 */
    private String description;

    /** データリスト */
    private List<String> data_list;

}
