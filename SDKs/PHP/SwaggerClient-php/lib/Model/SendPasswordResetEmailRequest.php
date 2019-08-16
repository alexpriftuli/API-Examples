<?php
/**
 * SendPasswordResetEmailRequest
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * MINDBODY Public API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: v6
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 2.4.6
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * SendPasswordResetEmailRequest Class Doc Comment
 *
 * @category Class
 * @description Request to send a password reset email to a user
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class SendPasswordResetEmailRequest implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'SendPasswordResetEmailRequest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'user_email' => 'string',
        'user_first_name' => 'string',
        'user_last_name' => 'string'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'user_email' => null,
        'user_first_name' => null,
        'user_last_name' => null
    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'user_email' => 'UserEmail',
        'user_first_name' => 'UserFirstName',
        'user_last_name' => 'UserLastName'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'user_email' => 'setUserEmail',
        'user_first_name' => 'setUserFirstName',
        'user_last_name' => 'setUserLastName'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'user_email' => 'getUserEmail',
        'user_first_name' => 'getUserFirstName',
        'user_last_name' => 'getUserLastName'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['user_email'] = isset($data['user_email']) ? $data['user_email'] : null;
        $this->container['user_first_name'] = isset($data['user_first_name']) ? $data['user_first_name'] : null;
        $this->container['user_last_name'] = isset($data['user_last_name']) ? $data['user_last_name'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['user_email'] === null) {
            $invalidProperties[] = "'user_email' can't be null";
        }
        if ($this->container['user_first_name'] === null) {
            $invalidProperties[] = "'user_first_name' can't be null";
        }
        if ($this->container['user_last_name'] === null) {
            $invalidProperties[] = "'user_last_name' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets user_email
     *
     * @return string
     */
    public function getUserEmail()
    {
        return $this->container['user_email'];
    }

    /**
     * Sets user_email
     *
     * @param string $user_email The user’s email address. The software uses this parameter as the username.
     *
     * @return $this
     */
    public function setUserEmail($user_email)
    {
        $this->container['user_email'] = $user_email;

        return $this;
    }

    /**
     * Gets user_first_name
     *
     * @return string
     */
    public function getUserFirstName()
    {
        return $this->container['user_first_name'];
    }

    /**
     * Sets user_first_name
     *
     * @param string $user_first_name The user’s first name. The software uses this parameter to verify the user.
     *
     * @return $this
     */
    public function setUserFirstName($user_first_name)
    {
        $this->container['user_first_name'] = $user_first_name;

        return $this;
    }

    /**
     * Gets user_last_name
     *
     * @return string
     */
    public function getUserLastName()
    {
        return $this->container['user_last_name'];
    }

    /**
     * Sets user_last_name
     *
     * @param string $user_last_name The user’s last name. The software uses this parameter to verify the user.
     *
     * @return $this
     */
    public function setUserLastName($user_last_name)
    {
        $this->container['user_last_name'] = $user_last_name;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}

