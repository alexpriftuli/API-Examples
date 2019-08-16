=begin
#MINDBODY Public API

#No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: v6

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.6

=end

require 'date'

module SwaggerClient
  class CheckoutShoppingCartRequest
    # The unique ID of the shopping cart to be processed. You can use this value to maintain a persistent cart. If you do not specify a cart ID, the MINDBODY software generates one.
    attr_accessor :cart_id

    # The RSSID of the client making the purchase. A cart can be validated without a client ID, but a client ID must be specified to complete a sale.
    attr_accessor :client_id

    # When `true`, indicates that the contents of the cart are validated, but the transaction does not take place. You should use this parameter during testing and when checking the calculated totals of the items in the cart.<br />  When `false`, the transaction takes place and the database is affected.<br />  Default: **false**
    attr_accessor :test

    # A list of the items in the cart.
    attr_accessor :items

    # When `true`, indicates that the cart is to be completed by a staff member and is to take place at one of the business’ physical locations.<br />  When `false`, indicates that the cart is to be completed by a client from the business’ online store.<br />  Default: **false**
    attr_accessor :in_store

    # Promotion code to be applied to the cart.
    attr_accessor :promotion_code

    # A list of payment information objects to be applied to payment against the items in the cart.
    attr_accessor :payments

    # When `true`, sends a purchase receipt email to the client. Note that all appropriate permissions and settings must be enabled for the client to receive an email.<br />  Default: **false**
    attr_accessor :send_email

    # The location ID to be used for pulling business mode prices and taxes. If no location ID is supplied, it defaults to the online store, represented by a null value.   Default: **null** (the online store)
    attr_accessor :location_id

    # The byte array data of the signature image.
    attr_accessor :image

    # The name of the signature image being uploaded.
    attr_accessor :image_file_name

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'cart_id' => :'CartId',
        :'client_id' => :'ClientId',
        :'test' => :'Test',
        :'items' => :'Items',
        :'in_store' => :'InStore',
        :'promotion_code' => :'PromotionCode',
        :'payments' => :'Payments',
        :'send_email' => :'SendEmail',
        :'location_id' => :'LocationId',
        :'image' => :'Image',
        :'image_file_name' => :'ImageFileName'
      }
    end

    # Attribute type mapping.
    def self.swagger_types
      {
        :'cart_id' => :'String',
        :'client_id' => :'String',
        :'test' => :'BOOLEAN',
        :'items' => :'Array<CheckoutItemWrapper>',
        :'in_store' => :'BOOLEAN',
        :'promotion_code' => :'String',
        :'payments' => :'Array<CheckoutPaymentInfo>',
        :'send_email' => :'BOOLEAN',
        :'location_id' => :'Integer',
        :'image' => :'String',
        :'image_file_name' => :'String'
      }
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      return unless attributes.is_a?(Hash)

      # convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      if attributes.has_key?(:'CartId')
        self.cart_id = attributes[:'CartId']
      end

      if attributes.has_key?(:'ClientId')
        self.client_id = attributes[:'ClientId']
      end

      if attributes.has_key?(:'Test')
        self.test = attributes[:'Test']
      end

      if attributes.has_key?(:'Items')
        if (value = attributes[:'Items']).is_a?(Array)
          self.items = value
        end
      end

      if attributes.has_key?(:'InStore')
        self.in_store = attributes[:'InStore']
      end

      if attributes.has_key?(:'PromotionCode')
        self.promotion_code = attributes[:'PromotionCode']
      end

      if attributes.has_key?(:'Payments')
        if (value = attributes[:'Payments']).is_a?(Array)
          self.payments = value
        end
      end

      if attributes.has_key?(:'SendEmail')
        self.send_email = attributes[:'SendEmail']
      end

      if attributes.has_key?(:'LocationId')
        self.location_id = attributes[:'LocationId']
      end

      if attributes.has_key?(:'Image')
        self.image = attributes[:'Image']
      end

      if attributes.has_key?(:'ImageFileName')
        self.image_file_name = attributes[:'ImageFileName']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      if @client_id.nil?
        invalid_properties.push('invalid value for "client_id", client_id cannot be nil.')
      end

      if @items.nil?
        invalid_properties.push('invalid value for "items", items cannot be nil.')
      end

      if @payments.nil?
        invalid_properties.push('invalid value for "payments", payments cannot be nil.')
      end

      if !@image.nil? && @image !~ Regexp.new(/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/)
        invalid_properties.push('invalid value for "image", must conform to the pattern /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/.')
      end

      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      return false if @client_id.nil?
      return false if @items.nil?
      return false if @payments.nil?
      return false if !@image.nil? && @image !~ Regexp.new(/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/)
      true
    end

    # Custom attribute writer method with validation
    # @param [Object] image Value to be assigned
    def image=(image)
      if !image.nil? && image !~ Regexp.new(/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/)
        fail ArgumentError, 'invalid value for "image", must conform to the pattern /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/.'
      end

      @image = image
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          cart_id == o.cart_id &&
          client_id == o.client_id &&
          test == o.test &&
          items == o.items &&
          in_store == o.in_store &&
          promotion_code == o.promotion_code &&
          payments == o.payments &&
          send_email == o.send_email &&
          location_id == o.location_id &&
          image == o.image &&
          image_file_name == o.image_file_name
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Fixnum] Hash code
    def hash
      [cart_id, client_id, test, items, in_store, promotion_code, payments, send_email, location_id, image, image_file_name].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.swagger_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :BOOLEAN
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        temp_model = SwaggerClient.const_get(type).new
        temp_model.build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        next if value.nil?
        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end
  end
end