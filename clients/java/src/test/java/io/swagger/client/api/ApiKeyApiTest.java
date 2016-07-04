/**
 * BitMEX API
 * REST API for the BitMEX.com trading platform.<br><br><a href=\"/app/restAPI\">REST Documentation</a><br><a href=\"/app/wsAPI\">Websocket Documentation</a>
 *
 * OpenAPI spec version: 1.2.0
 * Contact: support@bitmex.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


package io.swagger.client.api;

import io.swagger.client.ApiException;
import io.swagger.client.model.ApiKey;
import io.swagger.client.model.Error;
import io.swagger.client.model.InlineResponse200;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ApiKeyApi
 */
public class ApiKeyApiTest {

    private final ApiKeyApi api = new ApiKeyApi();

    
    /**
     * Disable an API Key.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiKeyDisableTest() throws ApiException {
        String apiKeyID = null;
        // ApiKey response = api.apiKeyDisable(apiKeyID);

        // TODO: test validations
    }
    
    /**
     * Enable an API Key.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiKeyEnableTest() throws ApiException {
        String apiKeyID = null;
        // ApiKey response = api.apiKeyEnable(apiKeyID);

        // TODO: test validations
    }
    
    /**
     * Get your API Keys.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiKeyGetTest() throws ApiException {
        Boolean reverse = null;
        // List<ApiKey> response = api.apiKeyGet(reverse);

        // TODO: test validations
    }
    
    /**
     * Create a new API Key.
     *
     * API Keys can also be created via [this Python script](https://github.com/BitMEX/market-maker/blob/master/generate-api-key.py) See the [API Key Documentation](/app/apiKeys) for more information on capabilities.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiKeyNewTest() throws ApiException {
        String name = null;
        String cidr = null;
        String permissions = null;
        Boolean enabled = null;
        String token = null;
        // ApiKey response = api.apiKeyNew(name, cidr, permissions, enabled, token);

        // TODO: test validations
    }
    
    /**
     * Remove an API Key.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void apiKeyRemoveTest() throws ApiException {
        String apiKeyID = null;
        // InlineResponse200 response = api.apiKeyRemove(apiKeyID);

        // TODO: test validations
    }
    
}