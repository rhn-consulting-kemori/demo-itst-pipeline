package com.redhat.example.rule;

// Util
import org.yaml.snakeyaml.Yaml;

// Spring
import org.springframework.stereotype.Component;

// Entity
import com.redhat.example.entity.ApiPostDataEntity;

@Component
public class ApiYamlToClassRule {

    /** Create PopJ Class */
    public ApiPostDataEntity getYamltoEntity(String entity_yaml) {
        // YAML Unmarshall
        Yaml yaml = new Yaml();
        ApiPostDataEntity doc = yaml.loadAs(entity_yaml, ApiPostDataEntity.class);
        return doc;
    }
}
