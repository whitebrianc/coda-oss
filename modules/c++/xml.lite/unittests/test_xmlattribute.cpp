/* =========================================================================
 * This file is part of io-c++
 * =========================================================================
 *
 * (C) Copyright 2004 - 2019, MDA Information Systems LLC
 *
 * io-c++ is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this program; If not,
 * see <http://www.gnu.org/licenses/>.
 *
 */

#include <string>

#include "io/StringStream.h"
#include <TestCase.h>

#include "xml/lite/MinidomParser.h"

static const std::string strXml = R"(
<root>
    <doc name="doc">
        <a a="a">TEXT</a>
        <values int="314" double="3.14" string="314"/>
    </doc>
</root>)";

struct test_MinidomParser final
{
    xml::lite::MinidomParser xmlParser;
    const xml::lite::Element* getRootElement()
    {
        io::StringStream ss;
        ss.stream() << strXml;

        xmlParser.parse(ss);
        const auto doc = xmlParser.getDocument();
        return doc->getRootElement();    
    }
};

TEST_CASE(test_getAttribute)
{
    test_MinidomParser xmlParser;
    const auto root = xmlParser.getRootElement();


    const auto& a = root->getElementByTagName("a", true /*recurse*/);
    std::string value;
    value = a.getAttributes().getValue("a");
    TEST_ASSERT_EQ("a", value);

    const auto result = a.getAttributes().getValue("a", value);
    TEST_ASSERT_TRUE(result);
    TEST_ASSERT_EQ("a", value);
}

TEST_CASE(test_getAttributeNotFound)
{
    test_MinidomParser xmlParser;
    const auto root = xmlParser.getRootElement();

    const auto& a = root->getElementByTagName("a", true /*recurse*/);
    std::string value;
    const auto result = a.getAttributes().getValue("not_found", value);
    TEST_ASSERT_FALSE(result);

    TEST_SPECIFIC_EXCEPTION(a.getAttributes().getValue("not_found"), except::NoSuchKeyException);
}

TEST_CASE(test_getAttributeValue)
{
    test_MinidomParser xmlParser;
    const auto root = xmlParser.getRootElement();

    const auto& values = root->getElementByTagName("values", true /*recurse*/);

    {
        int value;
        const auto result = getValue(values.getAttributes(), "int", value);
        TEST_ASSERT_TRUE(result);
        TEST_ASSERT_EQ(314, value);
    }
    {
        double value;
        const auto result = getValue(values.getAttributes(), "double", value);
        TEST_ASSERT_TRUE(result);
        TEST_ASSERT_EQ(3.14, value);
    }
    {
        std::string value;
        const auto result = getValue(values.getAttributes(), "string", value);
        TEST_ASSERT_TRUE(result);
        TEST_ASSERT_EQ("314", value);
    }
}

int main(int, char**)
{
    TEST_CHECK(test_getAttribute);
    TEST_CHECK(test_getAttributeNotFound);
    TEST_CHECK(test_getAttributeValue);
}
